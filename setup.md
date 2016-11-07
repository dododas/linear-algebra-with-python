## Site setup 

This document lists the steps to create and maintain this repository

### 1. Create github repository 

Log on to github and create a repository called `linear-algebra-with-python`

### 2. Create local folder

{% highlight bash %}
mkdir linear-algebra
cd linear-algebra
mkdir code # subfolder for source code files
{% endhighlight %}

### 3. Create a jekyll site

```
jekyll new . --force
```

Edit the `_config.yml` file and add the following line to it:
```
destination: linear-algebra-with-python
```

Next edit the Gemfile and add the following lines
```
source 'https://rubygems.org

group :jekyll_plugins do
  gem 'jekyll-katex'
end
```
Save this file and run
```
bundle update
```

Insert the following line into the file `_includes/head.html` between the `<head>` and `</head>` tags
```
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.css">
```

```
cd linear-algebra-with-python
touch .nojekyll
git init
git add . 
git commit -m "First commit"
git remote add origin https://github.com/dododas/linear-algebra-with-python.git
git push origin master
```

### 3. Create a gh-pages branch

```
git checkout -b gh-pages # switches to gh-pages branch
git push origin gh-pages
```

Go to repository settings on github.com and set `gh-page` as the default branch

Then delete the master branch locally and in the remote repository
```
git branch -d master # delete local branch
git push origin :master # delete remote branch
```

At this point the repository contains a single gh-pages branch. To push future changes use:
```
git push -u origin gh-pages
```

