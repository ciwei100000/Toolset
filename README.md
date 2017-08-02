# Toolset

### Keywordlookup/keywordlookup.py

```
usage: python keywordlookup.py [-h] [--ifile] [--ofile]
                        [--file_include_rule] [--file_exclude_rule]
                        [--pattern PATTERN] [--path_exclude_rule]

look for pattern in files

optional arguments:
  -h, --help            show this help message and exit
  --ifile IFILE, -i IFILE
                        The input file or directories, default is ./
  --ofile OFILE, -o OFILE
                        The file to store the results, default is
                        ./keywordlookup_output
  --file_include_rule FI, -fi FI
                        Use regular expression to include input filenames
  --file_exclude_rule FE, -fe FE
                        Use regular expression to exclude input filenames
  --pattern PATTERN, -p PATTERN
                        Use regular expression to define the pattern to look
                        for
  --path_exclude_rule PE, -pe PE
                        Use regular expression to exclude input file path
 ```
 
 用法：
 
 ```
 python keywordlookup.py [-h] [--ifile] [--ofile]
                        [--file_include_rule ] [--file_exclude_rule ]
                        [--pattern PATTERN] [--path_exclude_rule ]
 ifile:                 需要寻找关键词的文件路径
 ofile：                输出文件路径
 file_include_rule：    包括的文件名，使用正则表达式
 file_exclude_rule：    排除的文件名，使用正则表达式
 pattern：              关键词特征，使用正则表达式
 path_exclude_rule：    排除的路径，使用正则表达式
``` 
 
 
