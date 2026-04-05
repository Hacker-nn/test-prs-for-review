import os
import requests

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
PR_NUMBER    = os.environ["PR_NUMBER"]
REPO         = os.environ["REPO"]

def get_diff():
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.diff"
    }
    return requests.get(url, headers=headers).text

def review_with_groq(diff):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"""You are a senior code reviewer. Review this git diff.
Find bugs, security issues, and style problems.
Format your response as a clear markdown list.

Diff:
{diff[:6000]}
"""
    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()["choices"][0]["message"]["content"]

def post_comment(body):
    url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    requests.post(url, headers=headers, json={"body": body})

def main():
    print("Getting PR diff...")
    diff = get_diff()
    if not diff.strip():
        print("No diff found.")
        return
    print("Sending to Groq...")
    review = review_with_groq(diff)
    comment = f"## 🤖 AI Code Review (Groq + Llama)\n\n{review}"
    print("Posting comment...")
    post_comment(comment)
    print("Done!")

if __name__ == "__main__":
    main()
