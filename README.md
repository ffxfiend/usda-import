usda-import
===========

Simple python script to parse and import the USDA ASCII text data files into a sqlite DB. The script includes the SR26 Data Files.

Parsing the data files.
The following is straight from the PDF documention on using these
data files. Data files can be found here: https://www.ars.usda.gov/Services/docs.htm?docid=23634
     
ASCII files are delimited. All fields are separated by carets (^) and text fields are surrounded by tildes (~). A double caret (^^) or two carets and two tildes (~~) appear when a field is null or blank. Format descriptions include the name of each field, its type [N = numeric with width and number of decimals (w.d) or A = alphanumeric], and maximum record length. The actual length in the data files may be less and most likely will change in later releases. Values will be padded with trailing zeroes when imported into various software packages, depending on the formats used.



TODO
----

1. Expand to include all optional datafiles.
2. Optimize script
3. Find a better way to deal with the encoding?