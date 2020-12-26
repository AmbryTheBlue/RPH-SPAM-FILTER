eval $(ssh-agent -s)
ssh-add /home/ambry/.ssh/id_rsa_ambrojak
ssh-add /home/ambry/.ssh/id_rsa_ambry
git add .
git commit
#adding collaborator:
#Co-authored-by: Katerina Kucerova <kucerka7@fel.cvut.cz>
git push

#personal - My WSL is kinda broken
#in case of WSL internet issues, use:
#sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'

#push new branch and set it as upstream (so then it is enough to just "push" without parameteres)
# git push -u all preparations
