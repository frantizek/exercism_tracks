"""Functions to manage a users shopping cart items."""
def add_item(current_cart: dict, items_to_add: list) -> dict:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart.setdefault(item, 1)
    return current_cart


def read_notes(notes) -> dict:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    new_shopping_cart = {}
    for item in notes:
        if item in new_shopping_cart:
            new_shopping_cart[item] += 1
        else:
            new_shopping_cart.setdefault(item, 1)
    return new_shopping_cart


def update_recipes(ideas: dict, recipe_updates: dict) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart: dict) -> dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return sorted(cart.items())


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fullfilled_dict = {}
    for k, v in cart.items():
        fullfilled_dict[k] = [v, aisle_mapping[k][0], aisle_mapping[k][1]]
    return dict(sorted(fullfilled_dict.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for k in fulfillment_cart.keys():
        if store_inventory[k][0]:
            if store_inventory[k][0] > 0:
                if store_inventory[k][0] - fulfillment_cart[k][0] <= 0:
                    store_inventory[k][0] = 'Out of Stock'
                else:
                    store_inventory[k][0] -= fulfillment_cart[k][0]

    return store_inventory
