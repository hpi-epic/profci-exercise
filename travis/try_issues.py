import logging, os, requests, sys

logging.basicConfig(level=logging.DEBUG) #logging.WARNING
log = logging.getLogger(__name__)

repo = os.environ.get('TRAVIS_REPO_SLUG')
url = "https://github.com/%s/issues" % repo

try:
	log.debug("pinging github issues: {url}".format(url=url))
	r = requests.head(url)
	if r.status_code != 200:
		log.warning("Issues not enabled! ({code})".format(code=r.status_code))
		sys.exit(1)
except requests.ConnectionError:
	print("failed to connect")
	sys.exit(1)