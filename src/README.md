I have completed all the steps mentioned. The program reads from flows.txt and lookup.csv files, using the dstport and protocol to generate the desired output, and writes the results to output.txt. I have tested it with case insensitivity.6 for tcp,17 for udp,1 for icmp.


The sample flow logs include dstport values such as 49153, 49154, 49155, 49156, 49157, 49158, 80, 1024, 443, 23, 25, 110, 993, and 143, with the protocol being 6 (TCP) for all entries. However, the output you provided differs from the sample flow logs and lookup table. According to my program’s results and manual verification, there are only 8 untagged entries and no sv_P4. Additionally, the entries with dstport values of 49153, 49154, 49155, 49156, and 49157 are missing in the sample output.


illumio=>src=>flows.txt,lookup.csv,parse_logs.py,output.txt


To Run:
Ensure you have the required files (lookup.csv and flows.txt) in the specified directory (illumio/src).
Run the script by executing "python parse_logs.py" from the illumio/src directory.


Thank you for the wonderful assignment looking forward to your feedback!
