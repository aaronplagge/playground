#include <cstdlib>
#include <ctime>
#include <iostream>
#include <memory>

struct node {
  std::shared_ptr<node> next;
  int mynum{};
};

int main() {
  std::shared_ptr<node> head(new node{NULL,3});
  std::shared_ptr<node> end(head);

  std::srand(std::time(nullptr));
  int rand_num{};

  for (int i = 0; i < 10; i++) {
      rand_num = rand() % 1000;
      std::shared_ptr<node> new_node(new node{NULL, rand_num});
      end->next = new_node;
      end = new_node;
      new_node.reset();
  }

  std::shared_ptr<node> current_node(head);
  std::cout << current_node->mynum << std::endl;
  while (current_node->next) {
    current_node = current_node->next;
    std::cout << current_node->mynum << std::endl;
  }

  current_node.reset();
  end.reset();

  return 0;
}
