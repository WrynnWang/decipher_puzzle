# decipher_puzzle
### 24 Hours Challenge: Decipher Puzzle
Normally, during this stage, there will be a set of algorithm problems or real-world questions like developing a demo under the required time. This is the first time thatＩcome across a decipher problem. Although still have enough time before start handling it, I want to figure it out as soon as possible because of my curiosity, passion to learn, etc.

#### Project intro
- **full_version.zip**  is a zip file that contains all the files including the answer gif
- **raw_string.txt**    is the original puzzle string
- **base32_to_int.py**    is the func that convert the raw string to int value, range is 0 ~ 31.( **'='** is a padding char)
- **int_to_five_digits_binary.py**   is the func that convert the previous decoded int value into 5 digits binary value.
- **binary_to_two_digits_hex.py**   is the func that convert the previous decoded binary string into a final heximal string.
A **C language file**   is called inside this function to write the final hexadecimal string into a newly generated **eureka.gif** file, which is the final answer that we want. Also this python function call a **bash** command

#### How to use
- Everything was put together, simply run this under the root dir
        `$ python main.py`
    And a eureka.gif will automatically generate under the same dir.

#### Process
1. Although this is the first time thatＩtry to solve this kind question, the first idea is this string should be base64 encoded. I have experience with post/get base64 strings in the previous projects. However after observing all the chars in the raw string, I figure out that it is Base32 rather than Base64 because of there are only characters from A-Z and numbers 2-7.([4](https://en.wikipedia.org/wiki/Base32)),([5](https://en.wikipedia.org/wiki/Base64))
1. After cleaning all the space and newline characters, the whole string was decoded to ASCII. However, the result is not satisfying, because there are hexadecimal numbers out of ASCII range. This decoding is not the final solution.
1. Although the previous decoding process is not good, we can still notice that the first several characters are "GIF89a". Then learn these ([1](https://en.wikipedia.org/wiki/GIF#Example_GIF_file)),([2](http://www.onicos.com/staff/iz/formats/gif.html)),([3](http://zqlite.com/2017/11/15/gif-bytes-format/)) about GIF data Structure, GIF data decoded and encoded. We now figure out how to use the decoded hexadecimal string to generate a GIF file.
1. Then using some time to develop some python scripts and C language files to achieve the whole process.

#### Process Flow
```flow
st=>start: Raw String
op=>operation: Base32 converted to int
op1=>operation: int converted to 5 digits binary
op2=>operation: binary converted to 2 digits heximal
op3=>operation: echo heximal string into .gif file
e=>end: GIF answer

st->op->op1->op2->op3->e
```

#### References
1. - `<GIF Wiki>` : <https://en.wikipedia.org/wiki/GIF#Example_GIF_file>
1. - `<GIF Format>` : <http://www.onicos.com/staff/iz/formats/gif.html>
1. - `<GIF 字节解析>` : <http://zqlite.com/2017/11/15/gif-bytes-format/>
1. - `<base32 Wiki>` : <https://en.wikipedia.org/wiki/Base32>
1. - `<base64 Wiki>` : <https://en.wikipedia.org/wiki/Base64>


