class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return math.ceil(self.item_count() / self.items_per_page)

    def page_item_count(self, page_index):
        if page_index >= self.page_count() or page_index < 0:
            return -1
        start_index = page_index * self.items_per_page
        end_index = start_index + self.items_per_page
        return min(end_index, self.item_count()) - start_index

    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1
        return item_index // self.items_per_page