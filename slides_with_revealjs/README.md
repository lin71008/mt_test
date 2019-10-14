# Quick slides with reveal.js
## Introduction

~~Same as title.~~

## Guide

1. Create an empty file named 'index.html'.
2. init.

    ```html
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Slides Example</title>
        </head>
        <body>
            <!-- Something -->
        </body>
    </html>
    ```

3. Install `reveal.js`.
    - you can just clone `reveal.js` on GitHub and unzip at locate folder.
4. import `reveal.js` to your html file.

    ```html
    <head>
        <link rel="stylesheet" href="reveal.js/css/reset.css">  
        <link rel="stylesheet" href="reveal.js/css/reveal.css">
        <link rel="stylesheet" href="reveal.js/css/theme/black.css">
        <script src="reveal.js/js/reveal.js"></script>    
    </head>
    <body>
        <script>
                Reveal.initialize();
        </script>
    </body>
    ```

5. init.

    ```html
    <body>
        <div class="reveal">
            <div class="slides">
                <!-- Add slides at here. -->
            </div>
        </div>
    </body>
    ```

6. Add slides.

    ```html
    <div class="slides">
        <section>
            <h1>Slides Example</h1>
        </section>
        <section>
            <section>
                <h2>Introduction</h2>
            </section>
            <section>
                <del>Same as title</del>
            </section>
        </section>
    </div>
    ```

7. Code syntax highlighting
    - import `highlight.js`

    ```html
    <head>
        <link rel="stylesheet" href="reveal.js/lib/css/zenburn.css">
    </head>
    <body>
        <script>
            Reveal.initialize({dependencies:[{ src: 'reveal.js/plugin/highlight/highlight.js', async: true, condition: function() { return !!document.querySelector( 'pre code' ); }, callback: function() { hljs.initHighlightingOnLoad(); } }]});
        </script>
    </body>
    ```
    
    - usage

    ```html
    <pre><code class="python">print('hello')</code></pre>
    ```

8. Finish ?
    - [Example](https://github.com/lin71008/Testing-Area/slides_with_revealjs/example/index.html)
9. More Info.
    - View [**reveal.js**](https://github.com/hakimel/reveal.js) GitHub pages.
