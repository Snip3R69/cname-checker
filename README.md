# CNAME Checker
Hey there! This Python script is here to help you check the CNAME record for a list of subdomains. It uses the `dnspython` library to do its magic.

## Usage
To use the script, run the following command in your terminal or command prompt:

```
python3 cname.py -f /path/to/subdomains.txt
```

Make sure to replace `/path/to/subdomains.txt` with the actual path to your file containing the subdomains, one per line. The script will then check the CNAME record for each subdomain and print the ones that have a CNAME record. Any subdomains without a CNAME record will be ignored, so they can go cry in a corner.

If you want to save the output to a file (maybe you want to brag to your friends about your CNAME-finding skills?), you can use shell redirection (`>`):

```
python3 cname.py -f /path/to/subdomains.txt > output.txt
```

This will save the output of the script to a file named `output.txt`. Be sure to give it a cool name, like `cool-output.txt` or `awesome-results.txt`.

## Requirements
The script needs the `dnspython` package to do its thing. You can install it using pip:

```
pip install dnspython
```

Or, if you're feeling lazy (we don't judge), you can use the `requirements.txt` file included in this repository to install all the dependencies at once:

```
pip install -r requirements.txt
```

The `requirements.txt` file is like the script's shopping list. It tells pip what to buy, so it can make the script work. The only thing on the list is `dnspython`, but it's an important ingredient. Without it, the script won't be able to check any CNAME records, and that would be a real bummer.

Well, that's all for now. Have fun checking those CNAMEs! If you have any questions or suggestions, feel free to hit me up. I'm always here to help you rock your DNS game.
