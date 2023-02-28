#!/usr/bin/env python3

import argparse
import dns.resolver

# Parse command line arguments
parser = argparse.ArgumentParser(description='Check CNAME records of subdomains from a file')
parser.add_argument('-f', '--file', required=True, help='Path to the file containing subdomains')
args = parser.parse_args()

# Open the file containing subdomains
with open(args.file, 'r') as f:
    subdomains = f.read().splitlines()

# Check CNAME record for each subdomain
for subdomain in subdomains:
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        cname = str(answers[0].target)
        print(f'{subdomain} is a CNAME for {cname}')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        # Ignore subdomains with no CNAME record
        pass
