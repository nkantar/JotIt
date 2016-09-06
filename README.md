# JotIt

Super duper totes minimal file-based CMS

## Wat?

I started keeping a journal at work, writing down thoughts and things learned on a given day. I default to writing everything in [Markdown](https://daringfireball.net/projects/markdown/ 'Markdown'), and I didn't want to set up a static site generator of some sort for a variety of reasons, so I wrote a very minimal Flask-based CMS that does little more than render [GitHub Flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/ 'Writing on GitHub / Basic writing and formatting syntax').

## So, what do I do?

Well, you start by installing **JotIt** via `pip`:

```shell
pip install jotit
```

Then you make a file called `myawesomejournal.py` and place the following in it:

```python
from jotit import JotIt
jotit = JotIt().new_jotit()
jotit.run()
```

Then you make a file called `config.yml` and populate it with what you need. Here's a sample configuration:

```yaml
---
site_name: 'My Awesome Journal'
login_required: True
secret_key: 'somereallylongstringthatshouldbemadeupofrandomcharacters'
users:
    - username: 'foo'
      password_hash: '3b0746488c92b328aec7c1fbd359ea36c304c785139679fec2de43dbbd0a3739badef548de6981f9ace7340d9e0d85bc420eef7864a6af1edf813b535265ce5f'  # This is a sha512 hash for 'wat' (without quotes)
```

Now make a directory called `content/` and place your Markdown files in there. (Note: Only `.md` files are supported at the moment.)

Now you should be able to run `python myawesomejournal.py` and visit [http://localhost:5000](http://localhost:5000) to see your masterpiece!

## Should I use this?

Sure, why not?

Seriously, though, it's *v0.1*. That means this is the bare minimum anyone would define as even remotely useful. I make no guarantees that things won't drastically change in the (near) future. In fact, some major changes are definitely already planned.

*However*, your `content/` dir will be safe. Its expected structure *shouldn't* change. Go ahead and write to your heart's content!

## What's coming?

Oh, *lots* of stuff!

I know, I know, I said this is supposed to be a minimal CMS, but some other functionality may be worthwhile. Here are some things on my to-consider list:

- **Better default templates** - Something a little more palatable would be nice.
- **Custom template/static support** - Because no one wants a site that looks like garbage and/or everyone else's, right?
- **Support for other file extensions** - People write Markdown with all sorts of extensions (e.g., `.markdown`, `.mdown`, `.text`), so that'd be cool.
- **Support for other file types** - It's not particularly difficult and may not be entirely out of scope to support other formats (e.g., reStructuredText, Textile, HTML).
- **Example site** - Lead by example, they say...
- **Custom functionality** - It'd be cool if you could write your own plugins, special routes, and whatever else you need, right? Your own [Cloud To Butt Plus](https://chrome.google.com/webstore/detail/cloud-to-butt-plus/apmlngnhgbnjpajelfkmabhkfapgnoai 'Cloud To Butt Plus') coming in 3..2..1...

## I need help!

- IRC: [irc://chat.freenode.net:6667/jotit](https://webchat.freenode.net/?channels=%23jotit&uio=MTE9NzIaa '#jotit on freenode')
<!-- Commented out until it starts working.
- Mailing list: [mailto:jotit@librelist.com](jotit@librelist.com 'jotit@librelist.com')
-->

## I wanna' help!

Well, uhh, for now you can [create isues](https://github.com/nkantar/JotIt/issues/new 'New Issue'), submit pull requests, or [get in touch](mailto:nik@nkantar.com 'Email me') and go from there. :)
