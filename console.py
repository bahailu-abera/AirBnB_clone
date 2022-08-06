#!/usr/bin/python3
"""
 Module for the entry point of the command line interpreter
"""
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter """
    prompt = "(hbnb) "
    __my_cls_dict = {'BaseModel': BaseModel}
    __file_path = "file.json"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        "An end-of-file on input is passed back as the string 'EOF'."
        return True

    def emptyline(self):
        return False

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__my_cls_dict:
            print("** class doesn't exist **")
        else:
            cls = HBNBCommand.__my_cls_dict[arg]
            my_instance = cls()
            my_instance.save()
            print(my_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = parse(arg)

        if len(args) < 1:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.__my_cls_dict:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
        else:
            cls_name, cls_id = args[0], args[1]
            all_objs = storage.all()
            obj_id = cls_name + "." + cls_id
            if obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        for _ in range(2):
            args.append(None)
        args = args[:2]
        cls_name, cls_id = tuple(args)

        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.__my_cls_dict:
            print("** class doesn't exist **")
        elif cls_id is not None:
            obj_id = cls_name + "." + cls_id
            all_objs = storage.all()
            if obj_id in all_objs.keys():
                del all_objs[obj_id]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        all_objs = storage.all()
        lst_objs = []
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            str_obj = str(obj)
            cls_name = str_obj.split(']')[0][1:]
            if not arg or cls_name == arg:
                lst_objs.append(str_obj)

        if arg and len(lst_objs) == 0:
            print("** class doesn't exist **")
        else:
            print(lst_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = parse(arg)
        for _ in range(4):
            args.append(None)
        args = args[:4]
        cls_name, cls_id, attr_name, attr_value = tuple(args)

        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.__my_cls_dict:
            print("** class doesn't exist **")
        elif cls_id is not None:
            obj_id = cls_name + "." + cls_id
            all_objs = storage.all()
            if obj_id in all_objs.keys():
                if attr_name is None:
                    print("** attribute name missing **")
                elif attr_value is None:
                    print("** value missing **")
                else:
                    obj = all_objs[obj_id]
                    attr_value = attr_value.strip('"')
                    if getattr(obj, attr_name, 0) != 0:
                        attr_type = type(getattr(obj, attr_name))
                        setattr(obj, attr_name, attr_type(attr_value))
                    else:
                        setattr(obj, attr_name, attr_value)
                    storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")


def parse(arg):
    """ Convert a series of space separeted data to list """
    return arg.split()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
