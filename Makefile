ZIP=zip
eval:
	$(ZIP) ambroz-SPAM_FILTER_EVAL.zip quality.py confmat.py utils.py
final:
	echo "\033[31m Don't forget to add all files! \033[0m"
	$(ZIP) ambroz-kucerova-SPAM_FILTER_FINAL.zip myfilter.py basefilter.py utils.py corpus.py trainingcorpus.py emailutils.py
prez:
	echo Not implemented yet!
