import json 
import pprint

all = []
with open('work.txt') as fp:
    # line = fp.readline()
    # print(line)
    # data = json.loads(line)
    # print(len(data))
    for cnt, line in enumerate(fp):
        all = all + json.loads(line)
    #    print("Line {}: {}".format(cnt, line))

# with open('all.json', 'w', encoding='utf8') as json_file:
#     json.dump(all, json_file, ensure_ascii=False)  
# print(len(all))

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(all[0])

import pandas as pd

df = pd.io.json.json_normalize(all, sep='_')

del df['kind' ]
del df['etag' ]
# del df['id' ]
# del df['snippet_publishedAt' ]
del df['snippet_channelId']
# del df['snippet_title' ]
# del df['snippet_description']
# del df['snippet_thumbnails_default_url' ]
del df['snippet_thumbnails_default_width']
del df['snippet_thumbnails_default_height' ]
del df['snippet_thumbnails_medium_url']
del df['snippet_thumbnails_medium_width' ]
del df['snippet_thumbnails_medium_height']
del df['snippet_thumbnails_high_url' ]
del df['snippet_thumbnails_high_width']
del df['snippet_thumbnails_high_height' ]
del df['snippet_thumbnails_standard_url']
del df['snippet_thumbnails_standard_width']
del df['snippet_thumbnails_standard_height' ]
# del df['snippet_thumbnails_maxres_url']
del df['snippet_thumbnails_maxres_width' ]
del df['snippet_thumbnails_maxres_height']
del df['snippet_channelTitle' ]
del df['snippet_playlistId' ]
# del df['snippet_position']
del df['snippet_resourceId_kind' ]
# del df['snippet_resourceId_videoId']

df.to_csv('all.csv')