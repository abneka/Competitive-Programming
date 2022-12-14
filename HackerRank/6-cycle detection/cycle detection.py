def has_cycle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast and slow==fast:
            return 1
    return 0
