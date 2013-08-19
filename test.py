result = {'/dqhm/dealLoginOut.jsp': (9, 0.542), '/zdfindword/': (1, 0.196), '/ldjgcdbt/index.jsp': (2, 3.612), '/zdxdjx/faq.jsp': (1, 0.129)}
def sort(result):
    result_after_sort = []
    
    max_count = 0
    url_cursor = ''
    
    while(len(result) > 0):
        for key in result:
            temp = result[key]
            if int(temp[0]) > max_count:
                max_count = temp[0]
                url_cursor = key
        result_after_sort.append((url_cursor, result[url_cursor][0], result[url_cursor][1]))
        del result[url_cursor]
        max_count = 0
        url_cursor = ''
    return result_after_sort

if __name__ == '__main__':
    for temp in sort(result):
        print temp
