for i in {0..620}; do find ./*/*/* -maxdepth 0 -mtime -15 -type d -exec crab resubmit {} \;; sleep 600; done
