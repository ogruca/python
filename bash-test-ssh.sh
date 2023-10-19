# bash script for testing wan connections to a host in the cloud on port tcp/22
printf "==========================\n"
printf "===== TESTING SYDNEY LINKS ======\n"
printf "==========================\n"
printf "\n\n"
printf "===== shared services ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.96.5/22" && echo "10.116.96.5:22 tcp/22 is open" || echo "10.116.96.5:22 tcp/22 is closed"

printf "\n===== non-prod ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.64.4/22" && echo "10.116.64.4:22 tcp/22 is open" || echo "10.116.64.4:22 tcp/22 is closed"

printf "\n===== pre-prod ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.32.2/22" && echo "10.116.32.2:22 tcp/22 is open" || echo "10.116.32.2:22 tcp/22 is closed"

printf "\n===== prod ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.0.2/22" && echo "10.116.0.2:22 tcp/22 is open" || echo "10.116.0.2:22 tcp/22 is closed"


printf "\n\n"
printf "=============================\n"
printf "===== TESTING MELBOURNE LINKS ======\n"
printf "=============================\n"
printf "\n\n"
printf "===== shared services ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.112.5/22" && echo "10.116.113.5:22 tcp/22 is open" || echo "10.116.113.5:22 tcp/22 is closed"

printf "\n===== non-prod ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.80.3/22" && echo "10.116.80.3:22 tcp/22 is open" || echo "10.116.80.3:22 tcp/22 is closed"

printf "\n===== pre-prod ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.48.2/22" && echo "10.116.48.2:22 tcp/22 is open" || echo "10.116.48.2:22 tcp/22 is closed"

printf "\n===== prod ======\n"
timeout 2 bash -c "echo > /dev/tcp/10.116.16.2/22" && echo "10.116.16.2:22 tcp/22 is open" || echo "10.116.16.2:22 tcp/22 is closed"
