# Задание 1

```
git commit
git tag in
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout in
```

![image](https://github.com/user-attachments/assets/47eb1c49-739f-415b-90d3-7c2d6fbc6c6f)

# Задание 2

```
123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr
$ git init
Initialized empty Git repository in C:/Users/123/Downloads/4pr/.git/

123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ git config user.name "alndis"

123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ git config user.email "alndis@gmail.com"

123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ micro prog.py
bash: micro: command not found

123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ nano prog.py

123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ cat prog.py
test datas


123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ git add .
warning: in the working copy of 'prog.py', LF will be replaced by CRLF the next time Git touches it

123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   prog.py


123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ git commit -m "test commit"
[master (root-commit) 3c480e9] test commit
 1 file changed, 2 insertions(+)
 create mode 100644 prog.py

123@DESKTOP-0TAHG33 MINGW64 ~/Downloads/4pr (master)
$ git log --oneline
3c480e9 (HEAD -> master) test commit
```

# Задание 3

```
123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/123/4pr/coder1/.git/

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git config user.name "Coder1"

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git config user.email "Coder1@ex.com"

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ echo "test message" > prog.py

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git add .

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git commit -m 'add coder1'
[master (root-commit) fce76ee] add coder1
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ cd ..

123@DESKTOP-0TAHG33 MINGW64 ~/4pr
$ git init --bare server.git
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/123/4pr/server.git/

123@DESKTOP-0TAHG33 MINGW64 ~/4pr
$ cd coder1

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git remote add server ../server.git

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git remote -v
server  ../server.git (fetch)
server  ../server.git (push)

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git push server master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 213 bytes | 106.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
 * [new branch]      master -> master

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ cd ..

123@DESKTOP-0TAHG33 MINGW64 ~/4pr
$ git clone server.git coder2
Cloning into 'coder2'...
done.

123@DESKTOP-0TAHG33 MINGW64 ~/4pr
$ cd coder1

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ echo "info PROG1" >> readme.md

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git add .

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git commit -m 'coder1 info'
[master 476fbb1] coder1 info
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ git push server master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 274 bytes | 91.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
   fce76ee..476fbb1  master -> master

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder1
$ cd ../coder2

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ echo "info PROG2" >> readme.md

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git add .

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git config user.name "coder2"

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git config user.email "coder2@ex.ru"

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git commit -m 'coder2 info'
[master d0a3819] coder2 info
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git push origin master
To /home/123/4pr/server.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to '/home/123/4pr/server.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git pull --no-rebase origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 254 bytes | 6.00 KiB/s, done.
From /home/123/4pr/server
 * branch            master     -> FETCH_HEAD
   fce76ee..476fbb1  master     -> origin/master
Auto-merging readme.md
CONFLICT (add/add): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git add .

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git commit -m 'fixed read'
[master 207b16c] fixed read

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git push origin master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 598 bytes | 149.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To /home/123/4pr/server.git
   476fbb1..207b16c  master -> master

123@DESKTOP-0TAHG33 MINGW64 ~/4pr/coder2
$ git log --graph --all
*   commit 207b16c85c42897708e798a9f74ef87648793237 (HEAD -> master, origin/master, origin/HEAD)
|\  Merge: d0a3819 476fbb1
| | Author: coder2 <coder2@ex.ru>
| | Date:   Wed Nov 6 14:35:14 2024 +0300
| |
| |     fixed read
| |
| * commit 476fbb165fea756c9b69c63b486b2611e7264b84
| | Author: Coder1 <Coder1@ex.com>
| | Date:   Wed Nov 6 14:33:16 2024 +0300
| |
| |     coder1 info
| |
* | commit d0a381957d43e31fd5b01a1f5b6a84ce8738dba6
|/  Author: coder2 <coder2@ex.ru>
|   Date:   Wed Nov 6 14:34:22 2024 +0300
|
|       coder2 info
|
* commit fce76ee7c02475c502390437a7f0cfe95cc27244
  Author: Coder1 <Coder1@ex.com>
:
```

![image](https://github.com/user-attachments/assets/4b75e4ad-92bc-49e9-bc59-32ce5e21e61a)

# Задание 4

```py
import subprocess

def get_git_objects():
    objects = subprocess.check_output(['git', 'rev-list', '--all', '--objects'], text=True).splitlines()
    return objects

def display_object_content(objects):
    for obj in objects:
        obj_hash = obj.split()[0]
        try:
            content = subprocess.check_output(['git', 'cat-file', '-p', obj_hash], text=True)
            print(f"Object Hash: {obj_hash}")
            print(content)
            print("-" * 40)
        except subprocess.CalledProcessError as e:
            print(f"Error processing object {obj_hash}: {e}")

def main():
    objects = get_git_objects()
    display_object_content(objects)

if __name__ == "__main__":
    main()
```

![image](https://github.com/user-attachments/assets/0818d172-b509-481b-a4f7-8826362a1f2e)
