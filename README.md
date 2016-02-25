# typeformPython
A python wrapper for the typeform API

#Installation
Clone the repo </br>
<pre><code>git clone https://github.com/grobbie94/typeformPython.git </pre></code>
In the base directory run:
<pre><code>python setup.py install
</pre></code>


#Usage
<b>Instantiating a form object</b>
<pre><code>from typeformPython import typeform
tf = typeform(API_KEY)
exampleForm = tf.getForm(formKey)
</pre></code>

<b>Retrieving questions from a form object</b>
<pre><code>questionDict = exampleFrom.getQuestions()
</pre></code>
Returns a dictionary of the form {questionToken: Question Text}

<b>Retrieving responses from a form object</b>
<pre><code>responseDict = exampleForm.getAllCompletedResponses()
</pre></code>

Returns all responses in form: {responseToken: {questionToken: answerString....}}

<b> Get average rating of a rating or opinion question</b>
<pre><code>rating = exampleForm.getAverageRating(questionToken)
</pre></code>


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
