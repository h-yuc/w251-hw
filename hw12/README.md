# Homework 12:

1. How much disk space is used after step 4?

**31G was used after step 4.**

2. Did you parallelize the crawlers in step 4? If so, how?

**Yes, I parallelized the crawlers in step 4 by splitting the URLs files into three folders, and then parallelly called the crawler on each of the nodes.**

3. Describe the steps to de-duplicate the web pages you crawled.

**To de-duplicate the web pages I crawled, I used the function `lazynlp.dedup_lines`, which takes in a list of URLs files and de-duplicate each file against all previous files, and then save the processed files in outfold. Then I used `lazynlp.dedup_lines_from_new_file` to de-duplicate new files against previously processed files.**

4. Submit the list of files you that your LazyNLP spiders crawled (ls -la) 

**See `filelist.out.zip`.**