import xmlrpc.client

# Connection parameters
url = 'https://dataruba.com'
db = 'azureuser'
username = 'admin'
password = 'admin'


# Common endpoint
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# Authenticate
uid = common.authenticate(db, username, password, {})

# Object endpoint
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


partners = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[]])
print(partners)

# Fetching records from public.blog_post model
# Search for blog posts (can add conditions if needed)
blog_post_ids = models.execute_kw(db, uid, password, 'public.blog_post', 'search', [[]])

# Read the records
# Here, we specify which fields we want to read; adjust as needed
blog_posts = models.execute_kw(db, uid, password, 'public.blog_post', 'read', [blog_post_ids, ['id', 'name', 'content']])

# Print the blog posts
for post in blog_posts:
    print(post)
