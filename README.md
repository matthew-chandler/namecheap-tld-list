## Up-to-date list

The current up-to-date list (last updated on 2024-04-11) is stored in **TLDs.json** as an array.

## About project

This list only contains domains that can be registered under on [namecheap](namecheap.com), a popular domain registrar.

All complete lists of current [Top Level Domains (TLDs)](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains) that I could find online contained TLDs that could not be used by the general public, such as .visa which exclusively by [Visa](https://visa.com) and its affiliates. As such, these lists are not ideal for many applications, such as those that recommend currently-available domain names to users. 

## Updating the list

Since new TLDs are [constantly being released](https://tld-list.com/launch-schedule) by [ICANN](https://www.icann.org/), the American organization that coordinates TLDs, this list will become outdated. You can generate your own updated list by following the instructions below. Also feel free to create a pull request to update the list.

### Instructions

1. Download or clone this repository.
2. Download the HTML of the [namecheap full TLD list](https://www.namecheap.com/domains/full-tld-list/) and replace the contents of **domains.html** with the HTML. \
Make sure the "Type" and "Choose from" options are either set to "All" or your desired alternative set of TLDs.\
You can download HTML using the inspect tool, using a browser extension, or using any other method that allows you to capture the entire list.
3. Navigate to the repository and run `python3 extract_TLDs.py` in the command line. The list will be output as **TLDs.json**.

Please feel free to create an issue for this repository if you need anything.
