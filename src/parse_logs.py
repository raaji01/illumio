import csv
from collections import defaultdict

# Load the lookup table into a dictionary
def load_lookup_table(lookup_file):
    lookup_table = {}
    with open(lookup_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dstport = int(row['dstport'])
            protocol = row['protocol'].lower()
            tag = row['tag']
            lookup_table[(dstport, protocol)] = tag
    return lookup_table

# Parse the protocol number to its string equivalent
def parse_protocol(protocol_number):
    protocol_map = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp',
        # Add more protocol numbers as needed
    }
    return protocol_map.get(protocol_number, 'unknown')

# Process the flow logs and count tags and port/protocol combinations
def process_flow_logs(flow_log_file, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    untagged_count = 0

    with open(flow_log_file, 'r') as file:
        for line in file:
            fields = line.strip().split()
            if len(fields) >= 8:
                dstport = int(fields[6])
                protocol_number = fields[7]
                protocol = parse_protocol(protocol_number)

                # Find the tag in the lookup table
                tag = lookup_table.get((dstport, protocol), "Untagged")
                if tag == "Untagged":
                    untagged_count += 1
                else:
                    tag_counts[tag] += 1

                # Count the port/protocol combination
                port_protocol_counts[(dstport, protocol)] += 1

    # Add untagged count to tag_counts
    tag_counts["Untagged"] = untagged_count

    return tag_counts, port_protocol_counts

# Write the tag and port/protocol combination counts to a file and print to console
def write_counts_to_file_and_console(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w') as file:
        # Write to file and print to console
        file.write("Tag Counts:\n")
        print("Tag Counts:")
        file.write("Tag,Count\n")
        print("Tag,Count")
        for tag, count in sorted(tag_counts.items(), key=lambda x: (-x[1], x[0])):
            file.write(f"{tag},{count}\n")
            print(f"{tag},{count}")

        file.write("\nPort/Protocol Combination Counts:\n")
        print("\nPort/Protocol Combination Counts:")
        file.write("Port,Protocol,Count\n")
        print("Port,Protocol,Count")
        for (port, protocol), count in sorted(port_protocol_counts.items(), key=lambda x: (x[0], x[1])):
            file.write(f"{port},{protocol},{count}\n")
            print(f"{port},{protocol},{count}")

# Main execution
lookup_table = load_lookup_table('lookup.csv')
tag_counts, port_protocol_counts = process_flow_logs('flows.txt', lookup_table)
write_counts_to_file_and_console(tag_counts, port_protocol_counts, 'output.txt')
