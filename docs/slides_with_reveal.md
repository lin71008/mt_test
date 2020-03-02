# Quick slides with reveal.js

## 介紹

使用 `reveal.js` 來快速生成好看的簡報.

## 教學

1. 開一個新資料夾, `FOLDER-NAME`

2. 下載 `reveal.js` 至資料夾中.

3. 按照下面格式搭建一個簡單的 `HTML + reveal.js` 框架.

    ```html
    <!DOCTYPE HTML>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            
            <!-- <title>Edit slides title at here.</title> -->

            <link rel="stylesheet" href="reveal.js/css/reset.css">  
            <link rel="stylesheet" href="reveal.js/css/reveal.css">
            <link rel="stylesheet" href="reveal.js/css/theme/black.css">
            <script src="reveal.js/js/reveal.js"></script>    
            
            <link rel="stylesheet" href="reveal.js/lib/css/zenburn.css">
        </head>

        <body>
            <div class="reveal">
                <div class="slides">
                    <!-- Add slides at here. -->
                </div>
            </div>

            <script src="reveal.js/js/reveal.js"></script>
            <script>
            Reveal.initialize({
                    controls: true,
                    progress: true,
                    history: true,
                    center: true,

                    transition: 'slide', // none/fade/slide/convex/concave/zoom

                    // Optional reveal.js plugins
                    dependencies: [
                        { src: 'reveal.js/lib/js/classList.js', condition: function() { return !document.body.classList; } },
                        { src: 'reveal.js/plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                        { src: 'reveal.js/plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                        { src: 'reveal.js/plugin/highlight/highlight.js', async: true, condition: function() { return !!document.querySelector( 'pre code' ); }, callback: function() { hljs.initHighlightingOnLoad(); } },
                        { src: 'reveal.js/plugin/zoom-js/zoom.js', async: true },
                        { src: 'reveal.js/plugin/notes/notes.js', async: true }
                    ]
                });
        </script>
        </body>
    </html>
    ```

4. 添加簡報標題, 內容, ... 

    * 如同一般 `HTML` 的寫法.

    * 提供兩層簡報結構, 以 `<section>` 來進行分段.

    * 提供段落功能, 以 `class="fragment`來進行段落

    * 提供程式碼風格區塊, 預設以 `<pre><code class="lang">` 來進行標示.

    * 支持 `Markdown` 風格, 使用 `<section data-markdown>` 後, 於 `<script type="text/template">` 中進行編寫.

5. 挑一個喜歡的簡報風格, 轉場特效, ...

6. 完成拉.

## 參考資料

* [reveal.js](https://github.com/hakimel/reveal.js) 
* [Example](https://github.com/lin71008/Testing-Area/tree/master/slides_with_revealjs)