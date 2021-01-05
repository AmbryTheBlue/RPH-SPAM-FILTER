ZIP=zip
eval:
	$(ZIP) ambroz-SPAM_FILTER_EVAL.zip quality.py confmat.py utils.py
filter:
	$(ZIP) ambroz-kucerova-SPAM_FILTER.zip filter.py basefilter.py corpus.py utils.py utils_email.py utils_analyzer.py utils_cleaner.py
final:
	echo "\033[31m Don't forget to add all files! \033[0m"
	$(ZIP) ambroz-kucerova-SPAM_FILTER_FINAL.zip filter.py basefilter.py corpus.py utils.py utils_email.py utils_analyzer.py utils_cleaner.py
prez:
	$(zip) ambroz-kucerova-prezentace-SPAM_FILTER.zip presentation/report.pdf presentation/presentation.pdf
