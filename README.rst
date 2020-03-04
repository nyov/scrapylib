=========
scrapylib
=========

Overview
========

**This library is deprecated and unmaintained.**

Some of its components were moved to their own package:

+--------------------------+------------------------------------------------+
| Old location             | New location                                   |
+==========================+================================================+
| scrapylib.crawlera       | `scrapy-crawlera`_                             |
+--------------------------+------------------------------------------------+
| scrapylib.deltafetch     | `scrapy-deltafetch`_                           |
+--------------------------+------------------------------------------------+
| scrapylib.hcf            | `scrapy-hcf`_                                  |
+--------------------------+------------------------------------------------+
| scrapylib.magicfields    | `scrapy-magicfields`_                          |
+--------------------------+------------------------------------------------+
| scrapylib.querycleaner   | `scrapy-querycleaner`_                         |
+--------------------------+------------------------------------------------+
| scrapylib.splitvariants  | `scrapy-splitvariants`_                        |
+--------------------------+------------------------------------------------+

Remaining code in this repo:

- Processors: Some additional scrapy.loader.processors

- ConstraintsPipeline

- GUIDPipeline

- SpiderFieldPipeline

- SelectiveProxyMiddleware

- SpiderTraceMiddleware

- RedisQueue

.. _scrapy-crawlera: https://github.com/scrapy-plugins/scrapy-crawlera
.. _scrapy-deltafetch: https://github.com/scrapy-plugins/scrapy-deltafetch
.. _scrapy-hcf: https://github.com/scrapy-plugins/scrapy-hcf
.. _scrapy-magicfields: https://github.com/scrapy-plugins/scrapy-magicfields
.. _scrapy-querycleaner: https://github.com/scrapy-plugins/scrapy-querycleaner
.. _scrapy-splitvariants: https://github.com/scrapy-plugins/scrapy-splitvariants
