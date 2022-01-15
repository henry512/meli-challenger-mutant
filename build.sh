git clone https://github.com/henry512/meli-challenger-mutant.git meli-mutant
cd meli-mutant
git checkout main
git pull
docker build -t henry512/api-meli-mutants:latest .
cd ..
