# python_coder_decoder
<p>How to use:<br>
&nbsp;&nbsp;&nbsp;&nbsp;You must run the program with the following arguments:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- input file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(with extension if you're encoding it  |  If you're decoding, then you don't have to specify extension)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- output file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(without extension if you're encoding it  |  If you're decoding, then you must specify its original extension)<br>
&nbsp;&nbsp;&nbsp;&nbsp;Or you can specify it after start. (The input rules are the same)<br>
</p>
<p>How encoding/decoding work:<br>
&nbsp;&nbsp;&nbsp;&nbsp;I am generating a binary key (like this one: 1001100).<br>
&nbsp;&nbsp;&nbsp;&nbsp;Its length is determined by the longest line of data.<br>
&nbsp;&nbsp;&nbsp;&nbsp;After that I do the following transformations:<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;key&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> 10110010<br>
&nbsp;&nbsp;&nbsp;&nbsp;start string&nbsp;&nbsp;-> 10010110<br>
&nbsp;&nbsp;&nbsp;&nbsp;result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> 00100000<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Explanation: If the symbol in key is 1, then I change the number in the string (below this symbol).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If 0, then leave as it is.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Decoding works on the same principle.<br>
&nbsp;&nbsp;&nbsp;&nbsp;I take the key, which is the first line in the file, and perform the exact same operation, <br>
&nbsp;&nbsp;&nbsp;&nbsp;resulting in the original line.<br>
 </p>
