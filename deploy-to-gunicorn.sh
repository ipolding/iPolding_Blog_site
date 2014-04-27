lsof -t -i :8000 | while read line
do
	kill -9 $line
done

gunicorn iPolding_Blog.wsgi &
