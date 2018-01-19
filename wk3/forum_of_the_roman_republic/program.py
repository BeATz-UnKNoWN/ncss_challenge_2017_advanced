from exceptions import PermissionDenied
from forum import Forum
from thread import Thread
from post import Post

# This file does not need to contain any code. The marker is testing the
# three classes in post.py, thread.py, and forum.py


if __name__ == '__main__':
  # Test your code here. This will not be checked by the marker.
  # Here is the example from the question.
  forum = Forum()
  thread = forum.publish('Battle of Zela', 'Veni, vidi, vici!', 'Caesar')
  thread.set_tags(['battle', 'brag'], 'Caesar')
  thread.publish_post(Post('That was quick!', 'Amantius'))
  thread.publish_post(Post('Hardly broke a sweat.', 'Caesar'))
  thread.publish_post(Post('Any good loot?', 'Amantius'))

  # Search by author
  print("The contents of Caesar's posts:")
  caesar_posts = forum.search_by_author('Caesar')
  print(sorted([p.get_content() for p in caesar_posts]))
  print()

  # Edit content of an existing post
  existing = thread.get_posts()[0]
  existing.set_content('I came, I saw, I conquered!', 'Caesar')

  # Upvote a post:
  existing.upvote('Cleopatra')
  existing.upvote('Brutus')
  existing.upvote('Amantius')
  existing.upvote('Cleopatra')

  print("[{}](+{}) -- {}\n".format(
    existing.get_author(),
    existing.get_upvotes(),
    existing.get_content()
  ))

  # And some access control:
  try:
    thread.set_title('Hijacked!', 'Cleopatra')
  except PermissionDenied:
    print('Cleopatra was not allowed to hijack the thread.')
  first_post = Post('Veni, vidi, vici!', 'Caesar')
  thread = Thread('Battle of Zela', first_post)
  next_post = Post('Braggart!', 'Brutus')
  thread.publish_post(next_post)
  last_post = Post('Nice work.', 'Cleopatra')
  thread.publish_post(last_post)
  print([p.get_author() for p in thread.get_posts()])
  try:
    thread.remove_post(next_post, 'Brutus')
  except PermissionDenied:
    print('PermissionDenied incorrectly raised.')
  except:
    print('An exception that was not PermissionDenied was incorrectly raised!')
  else:
    print('Post by Brutus allowed to be removed.')
  print([p.get_author() for p in thread.get_posts()])
  forum = Forum()
  thread = forum.publish('Battle of Zela', 'Veni, vidi, vici!', 'Caesar')
  try:
    thread.set_tags(['battle'], 'Cleopatra')
  except PermissionDenied:
    print('PermissionDenied correctly raised.')
  except:
    print('An exception that was not PermissionDenied was incorrectly raised!')
  else:
    print('Cleopatra should not be allowed to change the tags.')
  print(thread.get_tags())
  try:
    thread.set_tags(['battle'], 'Caesar')
  except PermissionDenied:
    print('PermissionDenied incorrectly raised.')
  except:
    print('An exception that was not PermissionDenied was incorrectly raised!')
  else:
    print('Caesar correctly allowed to change the tags.')
  print(thread.get_tags())
  thread.set_tags(['battle', 'brag'], 'Caesar')
  print(thread.get_tags())
  thread.set_tags(['battle', 'battle', 'battle'], 'Caesar')
  print(thread.get_tags())
  thread.set_tags(['drama', 'battle', 'action', 'latin'], 'Caesar')
  print(thread.get_tags())
  thread.set_tags([], 'Caesar')
  print(thread.get_tags())