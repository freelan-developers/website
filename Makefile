default: build

clean:
	rm -rf build
	rm -f www.tar.gz

build: clean
	python website.py -f
	ln -s build www
	tar zcvf www.tar.gz www/*
	rm www

deploy: build
	scp www.tar.gz freelan@ftp.freelan.org:
	ssh freelan@ftp.freelan.org rm -rf www.backup
	ssh freelan@ftp.freelan.org mv www www.backup
	ssh freelan@ftp.freelan.org tar zxvf www.tar.gz
	ssh freelan@ftp.freelan.org rm www.tar.gz

run:
	python website.py
