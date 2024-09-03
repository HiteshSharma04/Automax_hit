def usr_listing_path(instance, filename):
    return f"user_{0}/listings/{1}".format(instance.seller.user.id, filename)
