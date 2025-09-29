import io
import zipfile # for unzipping files
import requests # for downloading files
import frontmatter # for parsing frontmatter documentation

import argparse

def read_repo_data(repo_owner, repo_name):
    """
    Download and parse all markdown files from a GitHub repository.
    
    Args:
        repo_owner: GitHub username or organization
        repo_name: Repository name
    
    Returns:
        List of dictionaries containing file content and metadata
    """
    prefix = 'https://codeload.github.com' 
    url = f'{prefix}/{repo_owner}/{repo_name}/zip/refs/heads/main'
    print(url)
    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise Exception(f"Failed to download repository: {resp.status_code}")

    repository_data = []
    zf = zipfile.ZipFile(io.BytesIO(resp.content))
    
    for file_info in zf.infolist():
        filename = file_info.filename
        filename_lower = filename.lower()

        if not (filename_lower.endswith('.md') 
            or filename_lower.endswith('.mdx')):
            continue
    
        try:
            with zf.open(file_info) as f_in:
                content = f_in.read().decode('utf-8', errors='ignore')
                post = frontmatter.loads(content)
                data = post.to_dict()
                data['filename'] = filename
                repository_data.append(data)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue
    
    zf.close()
    return repository_data


def main():
    parser = argparse.ArgumentParser(description="Download and parse GitHub repo markdown files.")
    parser.add_argument("repo_owner", help="GitHub username or organization")
    parser.add_argument("repo_name", help="Repository name")
    args = parser.parse_args()

    data = read_repo_data(args.repo_owner, args.repo_name)
    print(f"Documents from {args.repo_owner}/{args.repo_name}: {len(data)}")


if __name__ == "__main__":
    main()
