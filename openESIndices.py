import elasticsearch
import curator
#import sys
import argparse

def main():


    parser = argparse.ArgumentParser(description='Utility script for opening indices from elastic search clusters')
    parser.add_argument("clusterUrl", help="Provide the elasticsearch url with credentials if necessary e.g. http://<user>:<pass>@clusterurl<:port>")
    parser.add_argument("prefix", help="Provide the index prefix you are cleaning up e.g. logs-index")
    parser.add_argument('-f', '--dateFormat', help='Enter the date format on your index', default="%Y-%m-%d")
    parser.add_argument('-s', '--dateSource', help='Choose to filter the index by the name or by the creation_date', choices=['name', 'creation_date'], default="name")
    parser.add_argument('-d', '--daysToOpen', help="Enter the number of days you want to keep (default 90)", type=int, default=30)
    args = parser.parse_args()

    try:
        client = elasticsearch.Elasticsearch([args.clusterUrl])
        ilo = curator.IndexList(client)
        ilo.filter_by_regex(kind='prefix', value=args.prefix)
        ilo.filter_by_age(source=args.dateSource, direction='younger', timestring=args.dateFormat, unit='days', unit_count=args.daysToOpen)
        ilo.filter_closed(False)
        print 'opening...'
        print '\n'.join(ilo.all_indices)
        close_indices = curator.Open(ilo)
        close_indices.do_action()
        print "Successfullly opened indices"
    except curator.NoIndices:
        print "Nothing found meeting the criteria to open, check your prefix name and that there are items to open"

if __name__ == "__main__":
    #for debug purposes simulate args
    #sys.argv = ['openESIndices.py', 'url', 'logs-index', '-d', '30']
    #sys.argv = ['-h']
    main()
