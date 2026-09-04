# Magazine (CSS Grid) — solución paso a paso

Código completo de cada paso en `pasos/paso-NNN/`.

## Paso 1

> Begin with your standard HTML boilerplate. Add a `DOCTYPE` declaration, an `html` element specifying this page is in English, a `head` element, and a `body` element.
> 
> Add a `<meta>` tag with the appropriate `charset` and a `<meta>` tag for mobile responsiveness within the `head` element.

Cambio en `index.html`:

```diff
@@ -1,2 +1,10 @@
+<!DOCTYPE html>
+<html lang="en">
+  <head>
+    <meta charset="UTF-8" />
+    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
+  </head>
+  <body>
+  </body>
+</html>
 
-
```

Código completo tras este paso: `pasos/paso-001/`

## Paso 2

> Add a `title` element with the text `Magazine`, a `link` element for the `https://fonts.googleapis.com/css?family=Anton%7CBaskervville%7CRaleway&display=swap` font stylesheet, a `link` for the `https://use.fontawesome.com/releases/v5.8.2/css/all.css` FontAwesome stylesheet, and a `link` for your `./styles.css` stylesheet.
> 
> Your font stylesheet will load three separate fonts: `Anton`, `Baskervville`, and `Raleway`.

Cambio en `index.html`:

```diff
@@ -3,8 +3,19 @@
   <head>
     <meta charset="UTF-8" />
     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
+    <title>Magazine</title>
+    <link
+      href="https://fonts.googleapis.com/css?family=Anton%7CBaskervville%7CRaleway&display=swap"
+      rel="stylesheet"
+    />
+    <link
+      rel="stylesheet"
+      href="https://use.fontawesome.com/releases/v5.8.2/css/all.css"
+    />
+    <link rel="stylesheet" href="styles.css" />
   </head>
   <body>
+
   </body>
 </html>
 
```

Código completo tras este paso: `pasos/paso-002/`

## Paso 3

> Within your `body`, create a `main` element. Then in that element, create a `section` with a `class` set to `heading`.

Cambio en `index.html`:

```diff
@@ -15,7 +15,11 @@
     <link rel="stylesheet" href="styles.css" />
   </head>
   <body>
+    <main>
+      <section class="heading">
 
+      </section>
+    </main>
   </body>
 </html>
 
```

Código completo tras este paso: `pasos/paso-003/`

## Paso 4

> Within your `.heading` element, create a `header` element with the `class` set to `hero`.
> 
> In that element, create an `img` element with the `src` set to `https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png`, the `alt` set to `freecodecamp logo`, and the `class` set to `hero-img`.
> 
> The `loading` attribute on an `img` element can be set to `lazy` to tell the browser not to fetch the image resource until it is needed (as in, when the user scrolls the image into view). As an additional benefit, lazy loaded elements will not load until the non-lazy elements are loaded - this means users with slow internet connections can view the content of your page without having to wait for the images to load.
> 
> Give your new `img` element a `loading` attribute set to `lazy`.

Cambio en `index.html`:

```diff
@@ -17,7 +17,14 @@
   <body>
     <main>
       <section class="heading">
-
+        <header class="hero">
+          <img
+            src="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
+            alt="freecodecamp logo"
+            loading="lazy"
+            class="hero-img"
+          />
+        </header>
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-004/`

## Paso 5

> After your `img` element, add an `h1` element with the `class` set to `hero-title` and the text set to `OUR NEW CURRICULUM`, followed by a `p` element with the `class` set to `hero-subtitle` and the text set to `Our efforts to restructure our curriculum with a more project-based focus`.

Cambio en `index.html`:

```diff
@@ -24,6 +24,11 @@
             loading="lazy"
             class="hero-img"
           />
+          <h1 class="hero-title">OUR NEW CURRICULUM</h1>
+          <p class="hero-subtitle">
+            Our efforts to restructure our curriculum with a more project-based
+            focus
+          </p>
         </header>
       </section>
     </main>
```

Código completo tras este paso: `pasos/paso-005/`

## Paso 6

> Your image currently takes up a lot of space. To better see what you are working on, add a `width` attribute to the `img` element, with a value of `400`.
> 
> You will remove this later on when you have worked on the CSS.

Cambio en `index.html`:

```diff
@@ -23,6 +23,7 @@
             alt="freecodecamp logo"
             loading="lazy"
             class="hero-img"
+            width="400"
           />
           <h1 class="hero-title">OUR NEW CURRICULUM</h1>
           <p class="hero-subtitle">
@@ -30,6 +31,7 @@
             focus
           </p>
         </header>
+
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-006/`

## Paso 7

> After your `header` element, create a `div` with the `class` set to `author`.
> 
> Within that `div`, create a `p` element with the `class` set to `author-name` and give it the text `By freeCodeCamp`. Wrap the `freeCodeCamp` portion in an `a` element with the `href` set to `https://freecodecamp.org`, and the `target` set to `_blank`.
> 
> 
> Below that, add a second `p` element with the class `publish-date` and the text `March 7, 2019`.

Cambio en `index.html`:

```diff
@@ -31,7 +31,15 @@
             focus
           </p>
         </header>
-
+        <div class="author">
+          <p class="author-name">
+            By
+            <a href="https://freecodecamp.org" target="_blank"
+              >freeCodeCamp</a
+            >
+          </p>
+          <p class="publish-date">March 7, 2019</p>
+        </div>
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-007/`

## Paso 8

> The `Referer` HTTP header contains information about the address or URL of a page that a user might be visiting from. This information can be used in analytics to track how many users from your page visit freecodecamp.org, for example. Setting the `rel` attribute to `noreferrer` omits this information from the HTTP request. Give your `a` element a `rel` attribute set to `noreferrer`.

Cambio en `index.html`:

```diff
@@ -34,12 +34,13 @@
         <div class="author">
           <p class="author-name">
             By
-            <a href="https://freecodecamp.org" target="_blank"
+            <a href="https://freecodecamp.org" target="_blank" rel="noreferrer"
               >freeCodeCamp</a
             >
           </p>
           <p class="publish-date">March 7, 2019</p>
         </div>
+
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-008/`

## Paso 9

> Below your `.author` element, create a new `div` element with the class `social-icons`.
> 
> Add five `a` elements within that new `div`, and give them the following `href` attributes.
> 
> - The first `a` element should have an `href` set to `https://www.facebook.com/freecodecamp`.
> - The second `a` element should have an `href` set to `https://twitter.com/freecodecamp`.
> - The third `a` element should have an `href` set to `https://instagram.com/freecodecamp`.
> - The fourth `a` element should have an `href` set to `https://www.linkedin.com/school/free-code-camp`.
> - The fifth `a` element should have an `href` set to `https://www.youtube.com/freecodecamp`.

Cambio en `index.html`:

```diff
@@ -40,7 +40,18 @@
           </p>
           <p class="publish-date">March 7, 2019</p>
         </div>
-
+        <div class="social-icons">
+          <a href="https://www.facebook.com/freecodecamp/">
+          </a>
+          <a href="https://twitter.com/freecodecamp/">
+          </a>
+          <a href="https://instagram.com/freecodecamp">
+          </a>
+          <a href="https://www.linkedin.com/school/free-code-camp/">
+          </a>
+          <a href="https://www.youtube.com/freecodecamp">
+          </a>
+        </div>
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-009/`

## Paso 10

> Within each of your new `a` elements, add an `i` element and give them the following classes:
> 
> - Your first `i` element should have the class `fab fa-facebook-f`
> - Your second `i` element should have the class `fab fa-twitter`
> - Your third `i` element should have the class `fab fa-instagram`
> - Your fourth `i` element should have the class `fab fa-linkedin-in`
> - Your fifth `i` element should have the class `fab fa-youtube`

Cambio en `index.html`:

```diff
@@ -42,17 +42,23 @@
         </div>
         <div class="social-icons">
           <a href="https://www.facebook.com/freecodecamp/">
+            <i class="fab fa-facebook-f"></i>
           </a>
           <a href="https://twitter.com/freecodecamp/">
+            <i class="fab fa-twitter"></i>
           </a>
           <a href="https://instagram.com/freecodecamp">
+            <i class="fab fa-instagram"></i>
           </a>
           <a href="https://www.linkedin.com/school/free-code-camp/">
+            <i class="fab fa-linkedin-in"></i>
           </a>
           <a href="https://www.youtube.com/freecodecamp">
+            <i class="fab fa-youtube"></i>
           </a>
         </div>
       </section>
+
     </main>
   </body>
 </html>
```

Código completo tras este paso: `pasos/paso-010/`

## Paso 11

> Below your `.heading` element, create a new `section` element with the `class` set to `text`. Within that, create a `p` element with the `class` set to `first-paragraph` and the following text:
> 
> ```markup
> Soon the freeCodeCamp curriculum will be 100% project-driven learning. Instead of a series of coding challenges, you'll learn through building projects - step by step. Before we get into the details, let me emphasize: we are not changing the certifications. All 6 certifications will still have the same 5 required projects. We are only changing the optional coding challenges.
> ```

Cambio en `index.html`:

```diff
@@ -58,7 +58,11 @@
           </a>
         </div>
       </section>
-
+      <section class="text">
+        <p class="first-paragraph">
+          Soon the freeCodeCamp curriculum will be 100% project-driven learning. Instead of a series of coding challenges, you'll learn through building projects - step by step. Before we get into the details, let me emphasize: we are not changing the certifications. All 6 certifications will still have the same 5 required projects. We are only changing the optional coding challenges.
+        </p>
+      </section>
     </main>
   </body>
 </html>
```

Código completo tras este paso: `pasos/paso-011/`

## Paso 12

> Create another `p` element below your `.first-paragraph` element, and give it the following text:
> 
> ```markup
> After years - years - of pondering these two problems and how to solve them, I slipped, hit my head on the sink, and when I came to I had a revelation! A vision! A picture in my head! A picture of this! This is what makes time travel possible: the flux capacitor!
> ```

Cambio en `index.html`:

```diff
@@ -62,6 +62,10 @@
         <p class="first-paragraph">
           Soon the freeCodeCamp curriculum will be 100% project-driven learning. Instead of a series of coding challenges, you'll learn through building projects - step by step. Before we get into the details, let me emphasize: we are not changing the certifications. All 6 certifications will still have the same 5 required projects. We are only changing the optional coding challenges.
         </p>
+        <p>
+          After years - years - of pondering these two problems and how to solve them, I slipped, hit my head on the sink, and when I came to I had a revelation! A vision! A picture in my head! A picture of this! This is what makes time travel possible: the flux capacitor!
+        </p>
+
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-012/`

## Paso 13

> Add a third `p` element at the end of your `.text` element, and give it the following text:
> 
> ```markup
> It wasn't as dramatic as Doc's revelation in Back to the Future. It just occurred to me while I was going for a run. The revelation: the entire curriculum should be a series of projects. Instead of individual coding challenges, we'll just have projects, each with their own seamless series of tests. Each test gives you just enough information to figure out how to get it to pass. (And you can view hints if that isn't enough.)
> ```

Cambio en `index.html`:

```diff
@@ -65,6 +65,10 @@
         <p>
           After years - years - of pondering these two problems and how to solve them, I slipped, hit my head on the sink, and when I came to I had a revelation! A vision! A picture in my head! A picture of this! This is what makes time travel possible: the flux capacitor!
         </p>
+        <p>
+          It wasn't as dramatic as Doc's revelation in Back to the Future. It
+          just occurred to me while I was going for a run. The revelation: the entire curriculum should be a series of projects. Instead of individual coding challenges, we'll just have projects, each with their own seamless series of tests. Each test gives you just enough information to figure out how to get it to pass. (And you can view hints if that isn't enough.)
+        </p>
 
       </section>
     </main>
```

Código completo tras este paso: `pasos/paso-013/`

## Paso 14

> After the three `p` elements within your `.text` element, create a `blockquote` element. Within that, add an `hr` element, a `p` element with the `class` set to `quote`, and a second `hr` element.
> 
> Give the `.quote` element the text `The entire curriculum should be a series of projects`.

Cambio en `index.html`:

```diff
@@ -69,6 +69,13 @@
           It wasn't as dramatic as Doc's revelation in Back to the Future. It
           just occurred to me while I was going for a run. The revelation: the entire curriculum should be a series of projects. Instead of individual coding challenges, we'll just have projects, each with their own seamless series of tests. Each test gives you just enough information to figure out how to get it to pass. (And you can view hints if that isn't enough.)
         </p>
+        <blockquote>
+          <hr />
+          <p class="quote">
+            The entire curriculum should be a series of projects
+          </p>
+          <hr />
+        </blockquote>
 
       </section>
     </main>
```

Código completo tras este paso: `pasos/paso-014/`

## Paso 15

> Below your `blockquote` element, add another `p` element with the following text:
> 
> ```markup
> No more walls of explanatory text. No more walls of tests. Just one test at a time, as you build up a working project. Over the course of passing thousands of tests, you build up projects and your own understanding of coding fundamentals. There is no transition between lessons and projects, because the lessons themselves are baked into projects. And there's plenty of repetition to help you retain everything because - hey - building projects in real life has plenty of repetition.
> ```

Cambio en `index.html`:

```diff
@@ -76,6 +76,10 @@
           </p>
           <hr />
         </blockquote>
+        <p>
+          No more walls of explanatory text. No more walls of tests. Just one
+          test at a time, as you build up a working project. Over the course of passing thousands of tests, you build up projects and your own understanding of coding fundamentals. There is no transition between lessons and projects, because the lessons themselves are baked into projects. And there's plenty of repetition to help you retain everything because - hey - building projects in real life has plenty of repetition.
+        </p>
 
       </section>
     </main>
```

Código completo tras este paso: `pasos/paso-015/`

## Paso 16

> Create a fifth `p` element at the end of your `.text` element, and give it the following text:
> 
> ```markup
> The main design challenge is taking what is currently paragraphs of explanation and instructions and packing them into a single test description text. Each project will involve dozens of tests like this. People will be coding the entire time, rather than switching back and forth from "reading mode" to "coding mode".
> ```

Cambio en `index.html`:

```diff
@@ -80,7 +80,9 @@
           No more walls of explanatory text. No more walls of tests. Just one
           test at a time, as you build up a working project. Over the course of passing thousands of tests, you build up projects and your own understanding of coding fundamentals. There is no transition between lessons and projects, because the lessons themselves are baked into projects. And there's plenty of repetition to help you retain everything because - hey - building projects in real life has plenty of repetition.
         </p>
-
+        <p>
+          The main design challenge is taking what is currently paragraphs of explanation and instructions and packing them into a single test description text. Each project will involve dozens of tests like this. People will be coding the entire time, rather than switching back and forth from "reading mode" to "coding mode".
+        </p>
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-016/`

## Paso 17

> Create one final `p` element at the end of your `.text` element and give it the following text:
> 
> ```markup
> Instead of a series of coding challenges, people will be in their code editor passing one test after another, quickly building up a project. People will get into a real flow state, similar to what they experience when they build the required projects at the end of each certification. They'll get that sense of forward progress right from the beginning. And freeCodeCamp will be a much smoother experience.
> ```

Cambio en `index.html`:

```diff
@@ -83,7 +83,11 @@
         <p>
           The main design challenge is taking what is currently paragraphs of explanation and instructions and packing them into a single test description text. Each project will involve dozens of tests like this. People will be coding the entire time, rather than switching back and forth from "reading mode" to "coding mode".
         </p>
+        <p>
+          Instead of a series of coding challenges, people will be in their code editor passing one test after another, quickly building up a project. People will get into a real flow state, similar to what they experience when they build the required projects at the end of each certification. They'll get that sense of forward progress right from the beginning. And freeCodeCamp will be a much smoother experience.
+        </p>
       </section>
+
     </main>
   </body>
 </html>
```

Código completo tras este paso: `pasos/paso-017/`

## Paso 18

> Below your `.text` element, create a new `section` element and give it a `class` of `text text-with-images`. Within that, create an `article` element with a `class` set to `brief-history`, and an `aside` element with the `class` set to `image-wrapper`.

Cambio en `index.html`:

```diff
@@ -87,7 +87,12 @@
           Instead of a series of coding challenges, people will be in their code editor passing one test after another, quickly building up a project. People will get into a real flow state, similar to what they experience when they build the required projects at the end of each certification. They'll get that sense of forward progress right from the beginning. And freeCodeCamp will be a much smoother experience.
         </p>
       </section>
+      <section class="text text-with-images">
+        <article class="brief-history">
 
+        </article>
+        <aside class="image-wrapper"></aside>
+      </section>
     </main>
   </body>
 </html>
```

Código completo tras este paso: `pasos/paso-018/`

## Paso 19

> Within your `article` element, create an `h3` element with the `class` set to `list-title` and the text of `A Brief History`. Below that, create a `p` element with the text `Of the Curriculum`. Then create a `ul` element with the class `lists`.

Cambio en `index.html`:

```diff
@@ -89,7 +89,11 @@
       </section>
       <section class="text text-with-images">
         <article class="brief-history">
+          <h3 class="list-title">A Brief History</h3>
+          <p>Of the Curriculum</p>
+          <ul class="lists">
 
+          </ul>
         </article>
         <aside class="image-wrapper"></aside>
       </section>
```

Código completo tras este paso: `pasos/paso-019/`

## Paso 20

> Within your `ul` element, create six `li` elements. Add an `h4` element with a `class` set to `list-subtitle` and a `p` element to each of your `li` elements.
> 
> Then give the `h4` and `p` elements the following text content, in order, with each `h4` using what's on the left side of the colon, and each `p` using what's on the right:
> 
> - `V1 - 2014`: `We launched freeCodeCamp with a simple list of 15 resources, including Harvard's CS50 and Stanford's Database Class.`
> - `V2 - 2015`: `We added interactive algorithm challenges.`
> - `V3 - 2015`: `We added our own HTML+CSS challenges (before we'd been relying on General Assembly's Dash course for these).`
> - `V4 - 2016`: `We expanded the curriculum to 3 certifications, including Front-End, Back-End, and Data Visualization. They each had 10 required projects, but only the Front-End section had its own challenges. For the other certs, we were still using external resources like Node School.`
> - `V5 - 2017`: `We added the back-end and data visualization challenges.`
> - `V6 - 2018`: `We launched 6 new certifications to replace our old ones. This was the biggest curriculum improvement to date.`

Cambio en `index.html`:

```diff
@@ -92,10 +92,50 @@
           <h3 class="list-title">A Brief History</h3>
           <p>Of the Curriculum</p>
           <ul class="lists">
-
+            <li>
+              <h4 class="list-subtitle">V1 - 2014</h4>
+              <p>
+                We launched freeCodeCamp with a simple list of 15 resources,
+                including Harvard's CS50 and Stanford's Database Class.
+              </p>
+            </li>
+            <li>
+              <h4 class="list-subtitle">V2 - 2015</h4>
+              <p>We added interactive algorithm challenges.</p>
+            </li>
+            <li>
+              <h4 class="list-subtitle">V3 - 2015</h4>
+              <p>
+                We added our own HTML+CSS challenges (before we'd been relying
+                on General Assembly's Dash course for these).
+              </p>
+            </li>
+            <li>
+              <h4 class="list-subtitle">V4 - 2016</h4>
+              <p>
+                We expanded the curriculum to 3 certifications, including Front-End,
+                Back-End, and Data Visualization. They each had 10 required
+                projects, but only the Front-End section had its own challenges.
+                For the other certs, we were still using external resources like
+                Node School.
+              </p>
+            </li>
+            <li>
+              <h4 class="list-subtitle">V5 - 2017</h4>
+              <p>We added the back-end and data visualization challenges.</p>
+            </li>
+            <li>
+              <h4 class="list-subtitle">V6 - 2018</h4>
+              <p>
+                We launched 6 new certifications to replace our old ones. This
+                was the biggest curriculum improvement to date.
+              </p>
+            </li>
           </ul>
         </article>
-        <aside class="image-wrapper"></aside>
+        <aside class="image-wrapper">
+
+        </aside>
       </section>
     </main>
   </body>
```

Código completo tras este paso: `pasos/paso-020/`

## Paso 21

> Within your `aside` element, create two `img` elements, a `blockquote` element, and a third `img` element. Give the `blockquote` element a `class` set to `image-quote`.

Cambio en `index.html`:

```diff
@@ -134,7 +134,10 @@
           </ul>
         </article>
         <aside class="image-wrapper">
-
+          <img />
+          <img />
+          <blockquote class="image-quote"></blockquote>
+          <img />
         </aside>
       </section>
     </main>
```

Código completo tras este paso: `pasos/paso-021/`

## Paso 22

> Within the `.image-wrapper` element, give your first `img` element a `src` of `https://cdn.freecodecamp.org/testable-projects-fcc/images/random-quote-machine.png`, an `alt` of `image of the quote machine project`, a `class` of `image-1`, a `loading` attribute set to `lazy`, a `width` attribute of `600`, and a `height` attribute of `400`.

Cambio en `index.html`:

```diff
@@ -134,7 +134,14 @@
           </ul>
         </article>
         <aside class="image-wrapper">
-          <img />
+          <img
+            src="https://cdn.freecodecamp.org/testable-projects-fcc/images/random-quote-machine.png"
+            alt="image of the quote machine project"
+            loading="lazy"
+            class="image-1"
+            width="600"
+            height="400"
+          />
           <img />
           <blockquote class="image-quote"></blockquote>
           <img />
```

Código completo tras este paso: `pasos/paso-022/`

## Paso 23

> Within your `.image-wrapper` element, give the second `img` element a `src` of `https://cdn.freecodecamp.org/testable-projects-fcc/images/calc.png`, an `alt` of `image of a calculator project`, a `loading` attribute set to `lazy`, a `class` set to `image-2`, a `width` attribute set to `400`, and a `height` attribute set to `400`.

Cambio en `index.html`:

```diff
@@ -142,7 +142,14 @@
             width="600"
             height="400"
           />
-          <img />
+          <img
+            src="https://cdn.freecodecamp.org/testable-projects-fcc/images/calc.png"
+            alt="image of a calculator project"
+            loading="lazy"
+            class="image-2"
+            width="400"
+            height="400"
+          />
           <blockquote class="image-quote"></blockquote>
           <img />
         </aside>
```

Código completo tras este paso: `pasos/paso-023/`

## Paso 24

> Within your `.image-wrapper` element, give your third `img` element a `src` of `https://cdn.freecodecamp.org/testable-projects-fcc/images/survey-form-background.jpeg`, an `alt` of `four people working on code`, a `loading` attribute of `lazy`, a `class` set to `image-3`, a `width` attribute set to `600`, and a `height` attribute set to `400`.

Cambio en `index.html`:

```diff
@@ -150,8 +150,17 @@
             width="400"
             height="400"
           />
-          <blockquote class="image-quote"></blockquote>
-          <img />
+          <blockquote class="image-quote">
+
+          </blockquote>
+          <img
+            src="https://cdn.freecodecamp.org/testable-projects-fcc/images/survey-form-background.jpeg"
+            alt="four people working on code"
+            loading="lazy"
+            class="image-3"
+            width="600"
+            height="400"
+          />
         </aside>
       </section>
     </main>
```

Código completo tras este paso: `pasos/paso-024/`

## Paso 25

> Within your `.image-quote` element, nest an `hr` element, a `p` element and a second `hr` element. Give the `p` element a `class` set to `quote` and the text `The millions of people who are learning to code through freeCodeCamp will have an even better resource to help them learn these fundamentals.`.

Cambio en `index.html`:

```diff
@@ -151,7 +151,13 @@
             height="400"
           />
           <blockquote class="image-quote">
-
+            <hr />
+            <p class="quote">
+              The millions of people who are learning to code
+              through freeCodeCamp will have an even better resource to help
+              them learn these fundamentals.
+            </p>
+            <hr />
           </blockquote>
           <img
             src="https://cdn.freecodecamp.org/testable-projects-fcc/images/survey-form-background.jpeg"
```

Código completo tras este paso: `pasos/paso-025/`

## Paso 26

> To start your CSS, normalize the CSS rules by targeting all elements with `*`, including the `::before` and `::after` pseudo-selectors.
> 
> Set the `padding` and `margin` properties both to `0` and set the `box-sizing` property to `border-box`.

Cambio en `styles.css`:

```diff
@@ -1,2 +1,6 @@
+*, ::before, ::after {
+  padding: 0;
+  margin: 0;
+  box-sizing: border-box;
+}
 
-
```

Código completo tras este paso: `pasos/paso-026/`

## Paso 27

> Create an `html` selector and give it a `font-size` property set to `62.5%`. This will set the default font size for your web page to 10px (the browser default is 16px).
> 
> This will make it easier for you to work with `rem` units later, as `2rem` would be 20px.

Cambio en `styles.css`:

```diff
@@ -4,3 +4,7 @@
   box-sizing: border-box;
 }
 
+html {
+  font-size: 62.5%;
+}
+
```

Código completo tras este paso: `pasos/paso-027/`

## Paso 28

> Create a `body` selector. Set the `font-family` property to `Baskervville`, with a fallback of `serif`. Set the `color` property to `linen` and the `background-color` property to `rgb(20, 30, 40)`.

Cambio en `styles.css`:

```diff
@@ -8,3 +8,9 @@
   font-size: 62.5%;
 }
 
+body {
+  font-family: 'Baskervville', serif;
+  color: linen;
+  background-color: rgb(20, 30, 40);
+}
+
```

Código completo tras este paso: `pasos/paso-028/`

## Paso 29

> Create an `h1` selector, and set the `font-family` property to `Anton` with the fallback of `sans-serif`.

Cambio en `styles.css`:

```diff
@@ -14,3 +14,7 @@
   background-color: rgb(20, 30, 40);
 }
 
+h1 {
+  font-family: 'Anton', sans-serif;
+}
+
```

Código completo tras este paso: `pasos/paso-029/`

## Paso 30

> Create an `h2, h3, h4, h5, h6` selector. Give it a `font-family` property set to `Raleway` with a fallback of `sans-serif`.

Cambio en `styles.css`:

```diff
@@ -18,3 +18,7 @@
   font-family: 'Anton', sans-serif;
 }
 
+h2, h3, h4, h5, h6 {
+  font-family: 'Raleway', sans-serif;
+}
+
```

Código completo tras este paso: `pasos/paso-030/`

## Paso 31

> Create an `a` selector, and give it a `text-decoration` property set to `none` and a `color` property set to `linen`.

Cambio en `styles.css`:

```diff
@@ -22,3 +22,8 @@
   font-family: 'Raleway', sans-serif;
 }
 
+a {
+  text-decoration: none;
+  color: linen;
+}
+
```

Código completo tras este paso: `pasos/paso-031/`

## Paso 32

> Now you are ready to start putting together the grid layout. CSS Grid offers a two-dimensional grid-based layout, allowing you to center items horizontally and vertically while still retaining control to do things like overlap elements.
> 
> Begin by creating a `main` selector and giving it a `display` property set to `grid`.

Cambio en `styles.css`:

```diff
@@ -27,3 +27,7 @@
   color: linen;
 }
 
+main {
+  display: grid;
+}
+
```

Código completo tras este paso: `pasos/paso-032/`

## Paso 33

> Now you can style the layout of your grid. CSS Grid is similar to Flexbox in that it has a special property for both the parent and child elements. 
> 
> In this case, your parent element is the `main` element. Set the content to have a three-column layout by adding a `grid-template-columns` property with a value of `1fr 94rem 1fr`. This will create three columns where the middle column is `94rem` wide, and the first and last columns are both 1 fraction of the remaining space in the grid container.

Cambio en `styles.css`:

```diff
@@ -29,5 +29,6 @@
 
 main {
   display: grid;
+  grid-template-columns: 1fr 94rem 1fr;
 }
 
```

Código completo tras este paso: `pasos/paso-033/`

## Paso 34

> Use the `minmax` function to make your columns responsive on any device. The `minmax` function takes two arguments, the first being the minimum value and the second being the maximum. These values could be a length, percentage, `fr`, or even a keyword like `max-content`.
> 
> Wrap each of your already defined values of the `grid-template-columns` property in a `minmax` function, using each value as the second argument. The first argument should be `2rem`, `min-content`, and `2rem` respectively.

Cambio en `styles.css`:

```diff
@@ -29,6 +29,6 @@
 
 main {
   display: grid;
-  grid-template-columns: 1fr 94rem 1fr;
+  grid-template-columns: minmax(2rem, 1fr) minmax(min-content, 94rem) minmax(2rem, 1fr);
 }
 
```

Código completo tras este paso: `pasos/paso-034/`

## Paso 35

> To add space between rows in the grid layout, you can use the `row-gap` property. Give the `main` selector a `row-gap` property of `3rem`.

Cambio en `styles.css`:

```diff
@@ -30,5 +30,6 @@
 main {
   display: grid;
   grid-template-columns: minmax(2rem, 1fr) minmax(min-content, 94rem) minmax(2rem, 1fr);
+  row-gap: 3rem;
 }
 
```

Código completo tras este paso: `pasos/paso-035/`

## Paso 36

> Your magazine will have three primary sections. You already set the overall layout in the `main` rule, but you can adjust the placement in the child rules.
> 
> One option is the `grid-column` property, which is shorthand for `grid-column-start` and `grid-column-end`. The `grid-column` property tells the grid item which grid line to start and end at.
> 
> Create a `.heading` rule and set the `grid-column` property to `2 / 3`. This will tell the `.heading` element to start at grid line 2 and end at grid line 3.

Cambio en `styles.css`:

```diff
@@ -33,3 +33,7 @@
   row-gap: 3rem;
 }
 
+.heading {
+  grid-column: 2 / 3;
+}
+
```

Código completo tras este paso: `pasos/paso-036/`

## Paso 37

> Create a `.text` selector and give it a `grid-column` property set to `2 / 3`.

Cambio en `styles.css`:

```diff
@@ -37,3 +37,7 @@
   grid-column: 2 / 3;
 }
 
+.text {
+  grid-column: 2 / 3;
+}
+
```

Código completo tras este paso: `pasos/paso-037/`

## Paso 38

> For additional control over the layout of your content, you can have a CSS Grid within a CSS Grid.
> 
> Set the `display` property of your `.heading` selector to `grid`.

Cambio en `index.html`:

```diff
@@ -106,8 +106,8 @@
             <li>
               <h4 class="list-subtitle">V3 - 2015</h4>
               <p>
-                We added our own HTML+CSS challenges (before we'd been relying
-                on General Assembly's Dash course for these).
+                We added our own HTML+CSS challenges (before we'd been relying on
+                General Assembly's Dash course for these).
               </p>
             </li>
             <li>
@@ -127,8 +127,8 @@
             <li>
               <h4 class="list-subtitle">V6 - 2018</h4>
               <p>
-                We launched 6 new certifications to replace our old ones. This
-                was the biggest curriculum improvement to date.
+                We launched 6 new certifications to replace our old ones. This was
+                the biggest curriculum improvement to date.
               </p>
             </li>
           </ul>
@@ -153,9 +153,9 @@
           <blockquote class="image-quote">
             <hr />
             <p class="quote">
-              The millions of people who are learning to code
-              through freeCodeCamp will have an even better resource to help
-              them learn these fundamentals.
+              The millions of people who are learning to code through freeCodeCamp
+              will have an even better resource to help them learn these
+              fundamentals.
             </p>
             <hr />
           </blockquote>
```

Cambio en `styles.css`:

```diff
@@ -1,4 +1,6 @@
-*, ::before, ::after {
+*,
+::before,
+::after {
   padding: 0;
   margin: 0;
   box-sizing: border-box;
@@ -35,6 +37,7 @@
 
 .heading {
   grid-column: 2 / 3;
+  display: grid;
 }
 
 .text {
```

Código completo tras este paso: `pasos/paso-038/`

## Paso 39

> Now you can style the content of the `.heading` element with CSS Grid.
> 
> The CSS `repeat()` function is used to repeat a value, rather than writing it out manually, and is helpful for grid layouts. For example, setting the `grid-template-columns` property to `repeat(20, 200px)` would create 20 columns each `200px` wide.
> 
> Give your `.heading` element a `grid-template-columns` property set to `repeat(2, 1fr)` to create two columns of equal width.

Cambio en `styles.css`:

```diff
@@ -38,6 +38,7 @@
 .heading {
   grid-column: 2 / 3;
   display: grid;
+  grid-template-columns: repeat(2, 1fr);
 }
 
 .text {
```

Código completo tras este paso: `pasos/paso-039/`

## Paso 40

> Give your `.heading` selector a `row-gap` property set to `1.5rem`.

Cambio en `styles.css`:

```diff
@@ -39,6 +39,7 @@
   grid-column: 2 / 3;
   display: grid;
   grid-template-columns: repeat(2, 1fr);
+  row-gap: 1.5rem;
 }
 
 .text {
```

Código completo tras este paso: `pasos/paso-040/`

## Paso 41

> Remember that the `grid-column` property determines which columns an element starts and ends at. There may be times where you are unsure of how many columns your grid will have, but you want an element to stop at the last column. To do this, you can use `-1` for the end column.
> 
> Create a `.hero` selector and give it a `grid-column` property set to `1 / -1`. This will tell the element to span the full width of the grid.

Cambio en `styles.css`:

```diff
@@ -46,3 +46,7 @@
   grid-column: 2 / 3;
 }
 
+.hero {
+  grid-column: 1 / -1;
+}
+
```

Código completo tras este paso: `pasos/paso-041/`

## Paso 42

> Give the `.hero` selector a `position` property set to `relative`.

Cambio en `styles.css`:

```diff
@@ -48,5 +48,6 @@
 
 .hero {
   grid-column: 1 / -1;
+  position: relative;
 }
 
```

Código completo tras este paso: `pasos/paso-042/`

## Paso 43

> You should remove the temporary `width` attribute before writing the CSS for your `.hero-img`.

Cambio en `index.html`:

```diff
@@ -23,7 +23,6 @@
             alt="freecodecamp logo"
             loading="lazy"
             class="hero-img"
-            width="400"
           />
           <h1 class="hero-title">OUR NEW CURRICULUM</h1>
           <p class="hero-subtitle">
```

Cambio en `styles.css`:

```diff
@@ -35,6 +35,8 @@
   row-gap: 3rem;
 }
 
+
+
 .heading {
   grid-column: 2 / 3;
   display: grid;
```

Código completo tras este paso: `pasos/paso-043/`

## Paso 44

> Create an `img` selector and give it a `width` property set to `100%`, and an `object-fit` property set to `cover`.
> 
> The `object-fit` property tells the browser how to position the element within its container. In this case, `cover` will set the image to fill the container, cropping as needed to avoid changing the aspect ratio.

Cambio en `styles.css`:

```diff
@@ -35,7 +35,10 @@
   row-gap: 3rem;
 }
 
-
+img {
+  width: 100%;
+  object-fit: cover;
+}
 
 .heading {
   grid-column: 2 / 3;
```

Código completo tras este paso: `pasos/paso-044/`

## Paso 45

> Create a `.hero-title` selector and give it a `text-align` property set to `center`, a `color` property set to `orangered` and a `font-size` property set to `8rem`.

Cambio en `styles.css`:

```diff
@@ -56,3 +56,9 @@
   position: relative;
 }
 
+.hero-title {
+  text-align: center;
+  color: orangered;
+  font-size: 8rem;
+}
+
```

Código completo tras este paso: `pasos/paso-045/`

## Paso 46

> The subtitle also needs to be styled. Create a `.hero-subtitle` selector and give it a `font-size` property set to `2.4rem`, a `color` property set to `orangered`, and a `text-align` property set to `center`.

Cambio en `styles.css`:

```diff
@@ -62,3 +62,9 @@
   font-size: 8rem;
 }
 
+.hero-subtitle {
+  font-size: 2.4rem;
+  color: orangered;
+  text-align: center;
+}
+
```

Código completo tras este paso: `pasos/paso-046/`

## Paso 47

> Create an `.author` selector and give it a `font-size` property set to `2rem` and a `font-family` property set to `Raleway` with a fallback of `sans-serif`.

Cambio en `styles.css`:

```diff
@@ -68,3 +68,8 @@
   text-align: center;
 }
 
+.author {
+  font-size: 2rem;
+  font-family: "Raleway", sans-serif;
+}
+
```

Código completo tras este paso: `pasos/paso-047/`

## Paso 48

> Create a `.author-name a:hover` selector and give it a `background-color` property set to `#306203`.
> 
> This will create a hover effect only for the `a` element within the `.author-name`, showing the original freeCodeCamp green in the background.

Cambio en `styles.css`:

```diff
@@ -73,3 +73,7 @@
   font-family: "Raleway", sans-serif;
 }
 
+.author-name a:hover {
+  background-color: #306203;
+}
+
```

Código completo tras este paso: `pasos/paso-048/`

## Paso 49

> Create a `.publish-date` selector and give it a `color` property of `rgba(255, 255, 255, 0.5)`.

Cambio en `styles.css`:

```diff
@@ -77,3 +77,7 @@
   background-color: #306203;
 }
 
+.publish-date {
+  color: rgba(255, 255, 255, 0.5);
+}
+
```

Código completo tras este paso: `pasos/paso-049/`

## Paso 50

> Create a `.social-icons` selector. Give it a `display` property set to `grid`, and a `font-size` property set to `3rem`.

Cambio en `styles.css`:

```diff
@@ -81,3 +81,8 @@
   color: rgba(255, 255, 255, 0.5);
 }
 
+.social-icons {
+  display: grid;
+  font-size: 3rem;
+}
+
```

Código completo tras este paso: `pasos/paso-050/`

## Paso 51

> The default settings for CSS Grid will create additional rows as needed, unlike Flexbox. Give the `.social-icons` selector a `grid-template-columns` property set to `repeat(5, 1fr)` to arrange the icons in a single row.

Cambio en `styles.css`:

```diff
@@ -84,5 +84,6 @@
 .social-icons {
   display: grid;
   font-size: 3rem;
+  grid-template-columns: repeat(5, 1fr);
 }
 
```

Código completo tras este paso: `pasos/paso-051/`

## Paso 52

> If you wanted to add more social icons, but keep them on the same row, you would need to update `grid-template-columns` to create additional columns. As an alternative, you can use the `grid-auto-flow` property.
> 
> This property takes either `row` or `column` as the first value, with an optional second value of `dense`. `grid-auto-flow` uses an auto-placement algorithm to adjust the grid layout. Setting it to `column` will tell the algorithm to create new columns for content as needed. The `dense` value allows the algorithm to backtrack and fill holes in the grid with smaller items, which can result in items appearing out of order.
> 
> For your `.social-icons` selector, set the `grid-auto-flow` property to `column`.

Cambio en `styles.css`:

```diff
@@ -85,5 +85,6 @@
   display: grid;
   font-size: 3rem;
   grid-template-columns: repeat(5, 1fr);
+  grid-auto-flow: column;
 }
 
```

Código completo tras este paso: `pasos/paso-052/`

## Paso 53

> Now the auto-placement algorithm will kick in when you add a new icon element. However, the algorithm defaults the new column width to be `auto`, which will not match your current columns.
> 
> You can override this with the `grid-auto-columns` property. Give the `.social-icons` selector a `grid-auto-columns` property set to `1fr`.

Cambio en `styles.css`:

```diff
@@ -86,5 +86,6 @@
   font-size: 3rem;
   grid-template-columns: repeat(5, 1fr);
   grid-auto-flow: column;
+  grid-auto-columns: 1fr;
 }
 
```

Código completo tras este paso: `pasos/paso-053/`

## Paso 54

> Much like Flexbox, with CSS Grid you can align the content of grid items with `align-items` and `justify-items`. `align-items` will align child elements along the column axis, and `justify-items` will align child elements along the row axis.
> 
> Give the `.social-icons` selector an `align-items` property set to `center`.

Cambio en `styles.css`:

```diff
@@ -87,5 +87,6 @@
   grid-template-columns: repeat(5, 1fr);
   grid-auto-flow: column;
   grid-auto-columns: 1fr;
+  align-items: center;
 }
 
```

Código completo tras este paso: `pasos/paso-054/`

## Paso 55

> Give the `.text` selector a `font-size` property set to `1.8rem` and a `letter-spacing` property set to `0.6px`.

Cambio en `styles.css`:

```diff
@@ -49,6 +49,8 @@
 
 .text {
   grid-column: 2 / 3;
+  font-size: 1.8rem;
+  letter-spacing: 0.6px;
 }
 
 .hero {
```

Código completo tras este paso: `pasos/paso-055/`

## Paso 56

> Your `.text` element is not a CSS Grid, but you can create columns within an element without using Grid by using the `column-width` property.
> 
> Give your `.text` selector a `column-width` property set to `25rem`.

Cambio en `styles.css`:

```diff
@@ -51,6 +51,7 @@
   grid-column: 2 / 3;
   font-size: 1.8rem;
   letter-spacing: 0.6px;
+  column-width: 25rem;
 }
 
 .hero {
```

Código completo tras este paso: `pasos/paso-056/`

## Paso 57

> Magazines often use justified text in their printed content to structure their layout and control the flow of their content. While this works in printed form, justified text on websites can be an accessibility concern, for example presenting challenges for folks with dyslexia.
> 
> To make your project look like a printed magazine, give the `.text` selector a `text-align` property set to `justify`.

Cambio en `styles.css`:

```diff
@@ -52,6 +52,7 @@
   font-size: 1.8rem;
   letter-spacing: 0.6px;
   column-width: 25rem;
+  text-align: justify;
 }
 
 .hero {
```

Código completo tras este paso: `pasos/paso-057/`

## Paso 58

> The `::first-letter` pseudo-selector allows you to target the first letter in the text content of an element.
> 
> Create a `.first-paragraph::first-letter` selector and set the `font-size` property to `6rem`. Also give it a `color` property set to `orangered` to make it stand out.

Cambio en `styles.css`:

```diff
@@ -94,3 +94,8 @@
   align-items: center;
 }
 
+.first-paragraph::first-letter {
+  font-size: 6rem;
+  color: orangered;
+}
+
```

Código completo tras este paso: `pasos/paso-058/`

## Paso 59

> The other text has been shifted out of place. Move it into position by giving the `.first-paragraph::first-letter` selector a `float` property set to `left` and a `margin-right` property set to `1rem`.

Cambio en `styles.css`:

```diff
@@ -39,6 +39,8 @@
   width: 100%;
   object-fit: cover;
 }
+
+
 
 .heading {
   grid-column: 2 / 3;
@@ -97,5 +99,7 @@
 .first-paragraph::first-letter {
   font-size: 6rem;
   color: orangered;
+  float: left;
+  margin-right: 1rem;
 }
 
```

Código completo tras este paso: `pasos/paso-059/`

## Paso 60

> Create an `hr` selector, and give it a `margin` property set to `1.5rem 0`.

Cambio en `styles.css`:

```diff
@@ -40,7 +40,9 @@
   object-fit: cover;
 }
 
-
+hr {
+  margin: 1.5rem 0;
+}
 
 .heading {
   grid-column: 2 / 3;
```

Código completo tras este paso: `pasos/paso-060/`

## Paso 61

> To give the `hr` a color, you need to adjust the `border` property. Give the `hr` selector a `border` property set to `1px solid rgba(120, 120, 120, 0.6)`.

Cambio en `styles.css`:

```diff
@@ -42,6 +42,7 @@
 
 hr {
   margin: 1.5rem 0;
+  border: 1px solid rgba(120, 120, 120, 0.6);
 }
 
 .heading {
```

Código completo tras este paso: `pasos/paso-061/`

## Paso 62

> Create a `.quote` selector. Give it a `color` property set to `#00beef`, a `font-size` property set to `2.4rem`, and a `text-align` property set to `center`.

Cambio en `styles.css`:

```diff
@@ -106,3 +106,9 @@
   margin-right: 1rem;
 }
 
+.quote {
+  color: #00beef;
+  font-size: 2.4rem;
+  text-align: center;
+}
+
```

Código completo tras este paso: `pasos/paso-062/`

## Paso 63

> To make the quote text stand out more, give the `.quote` selector a `font-family` property set to `Raleway` with a fallback of `sans-serif`.

Cambio en `styles.css`:

```diff
@@ -110,5 +110,6 @@
   color: #00beef;
   font-size: 2.4rem;
   text-align: center;
+  font-family: "Raleway", sans-serif;
 }
 
```

Código completo tras este paso: `pasos/paso-063/`

## Paso 64

> A quote is not really a quote without proper quotation marks. You can add these with CSS pseudo selectors.
> 
> Create a `.quote::before` selector and set the `content` property to `"` with a space following it.
> 
> Also, create a `.quote::after` selector and set the `content` property to `"` with a space preceding it.

Cambio en `styles.css`:

```diff
@@ -113,3 +113,11 @@
   font-family: "Raleway", sans-serif;
 }
 
+.quote::before {
+  content: '" ';
+}
+
+.quote::after {
+  content: ' "';
+}
+
```

Código completo tras este paso: `pasos/paso-064/`

## Paso 65

> Now it's time to style your third `section`. Note that it has the `text` and `text-with-images` values for the `class` attribute, which means it is already inheriting the styles from your `.text` rule.
> 
> Create a `.text-with-images` selector and set the `display` property to `grid`.

Cambio en `styles.css`:

```diff
@@ -121,3 +121,7 @@
   content: ' "';
 }
 
+.text-with-images {
+  display: grid;
+}
+
```

Código completo tras este paso: `pasos/paso-065/`

## Paso 66

> You will need to have a column for text and a column for images. Give the `.text-with-images` selector a `grid-template-columns` property set to `1fr 2fr`. Also set the `column-gap` property to `3rem` to provide more spacing between the columns.

Cambio en `styles.css`:

```diff
@@ -123,5 +123,7 @@
 
 .text-with-images {
   display: grid;
+  grid-template-columns: 1fr 2fr;
+  column-gap: 3rem;
 }
 
```

Código completo tras este paso: `pasos/paso-066/`

## Paso 67

> Give the `.text-with-images` selector a `margin-bottom` property set to `3rem`.

Cambio en `styles.css`:

```diff
@@ -125,5 +125,6 @@
   display: grid;
   grid-template-columns: 1fr 2fr;
   column-gap: 3rem;
+  margin-bottom: 3rem;
 }
 
```

Código completo tras este paso: `pasos/paso-067/`

## Paso 68

> Create a `.lists` selector and set the `list-style-type` property to `none`. This will get rid of the bullet points on the list items.

Cambio en `styles.css`:

```diff
@@ -128,3 +128,7 @@
   margin-bottom: 3rem;
 }
 
+.lists {
+  list-style-type: none;
+}
+
```

Código completo tras este paso: `pasos/paso-068/`

## Paso 69

> Give the `.lists` selector a `margin-top` property set to `2rem`.

Cambio en `styles.css`:

```diff
@@ -130,5 +130,6 @@
 
 .lists {
   list-style-type: none;
+  margin-top: 2rem;
 }
 
```

Código completo tras este paso: `pasos/paso-069/`

## Paso 70

> Create a `.lists li` rule to target the list items within your `.lists` element. Give it a `margin-bottom` property set to `1.5rem`.

Cambio en `styles.css`:

```diff
@@ -133,3 +133,7 @@
   margin-top: 2rem;
 }
 
+.lists li {
+  margin-bottom: 1.5rem;
+}
+
```

Código completo tras este paso: `pasos/paso-070/`

## Paso 71

> Create a `.list-title, .list-subtitle` selector and set the `color` property to `#00beef`.

Cambio en `styles.css`:

```diff
@@ -137,3 +137,7 @@
   margin-bottom: 1.5rem;
 }
 
+.list-title, .list-subtitle {
+  color: #00beef;
+}
+
```

Código completo tras este paso: `pasos/paso-071/`

## Paso 72

> Time to style the last section of the magazine - the images.
> 
> The images are wrapped with an `aside` element using the `image-wrapper` class, so create an `.image-wrapper` selector. Set the `display` property to `grid`.

Cambio en `styles.css`:

```diff
@@ -141,3 +141,7 @@
   color: #00beef;
 }
 
+.image-wrapper {
+  display: grid;
+}
+
```

Código completo tras este paso: `pasos/paso-072/`

## Paso 73

> The images should be within a two column, three row layout.
> 
> Give the `.image-wrapper` selector a `grid-template-columns` property set to `2fr 1fr` and a `grid-template-rows` property set to `repeat(3, min-content)`. This will give our grid rows that adjust in height based on the content, but columns that remain a fixed width based on the container.

Cambio en `styles.css`:

```diff
@@ -143,5 +143,7 @@
 
 .image-wrapper {
   display: grid;
+  grid-template-columns: 2fr 1fr;
+  grid-template-rows: repeat(3, min-content);
 }
 
```

Código completo tras este paso: `pasos/paso-073/`

## Paso 74

> The `gap` property is a shorthand way to set the value of `column-gap` and `row-gap` at the same time. If given one value, it sets the `column-gap` and `row-gap` both to that value. If given two values, it sets the `row-gap` to the first value and the `column-gap` to the second.
> 
> Give the `.image-wrapper` selector a `gap` property set to `2rem`.

Cambio en `styles.css`:

```diff
@@ -145,5 +145,6 @@
   display: grid;
   grid-template-columns: 2fr 1fr;
   grid-template-rows: repeat(3, min-content);
+  gap: 2rem;
 }
 
```

Código completo tras este paso: `pasos/paso-074/`

## Paso 75

> The `place-items` property can be used to set the `align-items` and `justify-items` values at the same time. The `place-items` property takes one or two values. If one value is provided, it is used for both the `align-items` and `justify-items` properties. If two values are provided, the first value is used for the `align-items` property and the second value is used for the `justify-items` property.
> 
> Give the `.image-wrapper` selector a `place-items` property set to `center`.

Cambio en `styles.css`:

```diff
@@ -146,5 +146,6 @@
   grid-template-columns: 2fr 1fr;
   grid-template-rows: repeat(3, min-content);
   gap: 2rem;
+  place-items: center;
 }
 
```

Código completo tras este paso: `pasos/paso-075/`

## Paso 76

> Create an `.image-1, .image-3` rule and give it a `grid-column` property set to `1 / -1`. This will allow the first and third images to span the full width of the grid.

Cambio en `styles.css`:

```diff
@@ -149,3 +149,7 @@
   place-items: center;
 }
 
+.image-1, .image-3 {
+  grid-column: 1 / -1;
+}
+
```

Código completo tras este paso: `pasos/paso-076/`

## Paso 77

> Now that the magazine layout is finished, you need to make it responsive.
> 
> Start with a `@media` query for `only screen` with a `max-width` of `720px`. Inside, create an `.image-wrapper` selector and give it a `grid-template-columns` property of `1fr`.
> 
> This will collapse the three images into one column on smaller screens.

Cambio en `styles.css`:

```diff
@@ -153,3 +153,9 @@
   grid-column: 1 / -1;
 }
 
+@media only screen and (max-width: 720px) {
+  .image-wrapper {
+    grid-template-columns: 1fr;
+  }
+}
+
```

Código completo tras este paso: `pasos/paso-077/`

## Paso 78

> Create another `@media` query for `only screen` with a `max-width` of `600px`. Within, create a `.text-with-images` rule and give it a `grid-template-columns` property of `1fr`.
> 
> This will collapse your bottom text area into a single column on smaller screens.

Cambio en `styles.css`:

```diff
@@ -159,3 +159,9 @@
   }
 }
 
+@media only screen and (max-width: 600px) {
+  .text-with-images {
+    grid-template-columns: 1fr;
+  }
+}
+
```

Código completo tras este paso: `pasos/paso-078/`

## Paso 79

> Create a third `@media` query for `only screen` with a `max-width` of `550px`. Within, create a `.hero-title` selector with a `font-size` set to `6rem`, a `.hero-subtitle, .author, .quote, .list-title` selector with a `font-size` set to `1.8rem`, a `.social-icons` selector with a `font-size` set to `2rem`, and a `.text` selector with a `font-size` set to `1.6rem`.

Cambio en `styles.css`:

```diff
@@ -165,3 +165,24 @@
   }
 }
 
+@media only screen and (max-width: 550px) {
+  .hero-title {
+    font-size: 6rem;
+  }
+
+  .hero-subtitle,
+  .author,
+  .quote,
+  .list-title {
+    font-size: 1.8rem;
+  }
+
+  .social-icons {
+    font-size: 2rem;
+  }
+
+  .text {
+    font-size: 1.6rem;
+  }
+}
+
```

Código completo tras este paso: `pasos/paso-079/`

## Paso 80

> Create one final `@media` query for `only screen` with a `max-width` of `420px`. Within, create a `.hero-title` selector with a `font-size` property set to `4.5rem`.
> 
> Congratulations! Your magazine is now complete.

Código completo tras este paso: `pasos/paso-080/`
