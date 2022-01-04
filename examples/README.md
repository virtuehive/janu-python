# Janu-net Python examples

## Start instructions

   ```bash
   python3 <example.py>
   ```

   Each example accepts the `-h` or `--help` option that provides a description of its arguments and their default values.

   If you run the tests against the janu router running in a Docker container, you need to add the
   `-e tcp/localhost:7447` option to your examples. That's because Docker doesn't support UDP multicast
   transport, and therefore the janu scouting and discrovery mechanism cannot work with.

## Examples description

### j_scout

   Scouts for janu peers and routers available on the network.

   Typical usage:
   ```bash
      python3 j_scout.py
   ```

### j_info

   Gets information about the janu-net session.

   Typical usage:
   ```bash
      python3 j_info.py
   ```


### j_put

   Puts a path/value into Janu.  
   The path/value will be received by all matching subscribers, for instance the [j_sub](#j_sub)
   and [j_storage](#j_storage) examples.

   Typical usage:
   ```bash
      python3 j_put.py
   ```
   or
   ```bash
      python3 j_put.py -p /demo/example/test -v 'Hello World'
   ```

### j_pub

   Declares a resource with a path and a publisher on this resource. Then puts a value using the numerical resource id.
   The path/value will be received by all matching subscribers, for instance the [j_sub](#j_sub)
   and [j_storage](#j_storage) examples.

   Typical usage:
   ```bash
      python3 j_pub.py
   ```
   or
   ```bash
      python3 j_pub.py -p /demo/example/test -v 'Hello World'
   ```

### j_sub

   Creates a subscriber with a key expression.  
   The subscriber will be notified of each put made on any key expression matching
   the subscriber's key expression, and will print this notification.

   Typical usage:
   ```bash
      python3 j_sub.py
   ```
   or
   ```bash
      python3 j_sub.py -s /demo/**
   ```

### j_pull

   Creates a pull subscriber with a selector.  
   The pull subscriber will receive each put made on any key expression matching
   the subscriber's key expression and will pull on demand and print the received
   key/value.

   Typical usage:
   ```bash
      python3 j_pull.py
   ```
   or
   ```bash
      python3 j_pull.py -s /demo/**
   ```

### j_get

   Sends a query message for a selector.  
   The queryables with a matching path or selector (for instance [j_eval](#j_eval) and [j_storage](#j_storage))
   will receive this query and reply with paths/values that will be received by the query callback.

   Typical usage:
   ```bash
      python3 j_get.py
   ```
   or
   ```bash
      python3 j_get.py -s /demo/**
   ```

### j_eval

   Creates a queryable function with a key expression.  
   This queryable function will be triggered by each call to a get operation on janu
   with a selector that matches the key expression, and will return a value to the querier.

   Typical usage:
   ```bash
      python3 j_eval.py
   ```
   or
   ```bash
      python3 j_eval.py -p /demo/example/eval -v 'This is the result'
   ```

### j_storage

   Trivial implementation of a storage in memory.  
   This examples creates a subscriber and a queryable on the same key expression.
   The subscriber callback will store the received key/values in an hashmap.
   The queryable callback will answer to queries with the key/values stored in the hashmap
   and that match the queried selector.

   Typical usage:
   ```bash
      python3 j_storage.py
   ```
   or
   ```bash
      python3 j_storage.py -s /demo/**
   ```

### j_pub_thr & j_sub_thr

   Pub/Sub throughput test.
   This example allows to perform throughput measurements between a pubisher performing
   put operations and a subscriber receiving notifications of those puts.

   Typical Subscriber usage:
   ```bash
      python3 j_sub_thr.py
   ```

   Typical Publisher usage:
   ```bash
      python3 j_pub_thr.py 1024
   ```