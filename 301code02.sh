#!/bin/bash

# Get current date and time
current_date=$(date +"%Y%m%d_%H%M%S")

# Copy /var/log/syslog to the current working directory
cp /var/log/syslog ./syslog_${current_date}
