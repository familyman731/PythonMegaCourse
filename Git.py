import subprocess as sub

sub.call("git status")

update = input("\nDo you want to push(1), pull(2), or exit(3)?")

if update == '1':
	sub.call("git add .")
	sub.call("git commit")
	sub.call("git push")

elif update == '2':
			sub.call("git pull")

input("Press any key to exit...")