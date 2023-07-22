# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides ...
============================================

Todo:
-----

Links:
------
- https://pyzotero.readthedocs.io/en/latest/#read-api-methods

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
import os

# Import | Libraries
from pyzotero import zotero

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

ZOTERO_LIBRARY_ID = "5128635"
ZOTERO_LIBRARY_TYPE = "group"
ZOTERO_API_KEY = os.getenv("ZOTERO_API_KEY", "")


# =============================================================================
# Functons
# =============================================================================

def getZotero():
    """
    """
    zot = zotero.Zotero(
        library_id = ZOTERO_LIBRARY_ID,
        library_type = ZOTERO_LIBRARY_TYPE,
        api_key = ZOTERO_API_KEY,
    )
    return zot


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    zot = getZotero()

    # items = zot.top(limit=5)
    # items = zot.top()
    items = zot.items()

    collections = zot.collections()


    # we've retrieved the latest five top-level items in our library
    # we can print each item's item type and ID
    for item in items:
        print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))