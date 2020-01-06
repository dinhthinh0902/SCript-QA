.PHONY: all run exportXL onlyrun
all: run exportXL

onlyrun:
	python3 main.py

run:
# 	rm export/report-log.txt
	python3 -u main.py |tee export/report-log.txt
# 	mydate=$(date +"%D %T")
# 	filename="export/1/report-log-"$mydate
# 	cp export/report-log.txt "export/log/"
# 	mv export/log/report-log.txt export/log/report-log-$mydate$.txt
exportXL:
	python3 -u export/export.py
