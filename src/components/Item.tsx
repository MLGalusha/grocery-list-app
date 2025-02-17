import { ItemType } from "../types";

interface ItemProps {
  item: ItemType;
  itemList: ItemType[];
  onModifyItemList: (itemList: ItemType[]) => void;
}

export default function Item({ item, itemList, onModifyItemList }: ItemProps) {
  function deleteItem() {
    const newList = itemList.filter((i) => i.id !== item.id);
    onModifyItemList(newList);
  }

  return (
    <div>
      <li>
        {item.text}
        <button onClick={() => deleteItem()}>Delete</button>
      </li>
    </div>
  );
}
