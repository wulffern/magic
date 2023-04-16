

all:
	test -d tmp || mkdir tmp
	python3 genposts.py


jstart:
	 docker run --rm --name magic_docs --volume="${PWD}:/srv/jekyll" -p 3003:4000 -it jekyll/jekyll:3.8 jekyll serve --watch --drafts

clean:
	rm -rf _tutorials/*
	rm -rf _man/*
	rm -rf tmp
