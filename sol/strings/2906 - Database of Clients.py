# 2906 - Database of Clients
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2906


def main():
    n = int(input())

    unique_users = set()
    for _ in range(n):
        localpart, provider = input().split("@")
        email_preffix = localpart.split("+")[0]
        email_preffix = email_preffix.replace(".", "")
        unique_users.add(f"{email_preffix}@{provider}")

    print(len(unique_users))


if __name__ == "__main__":
    main()
