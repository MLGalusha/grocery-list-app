import { useState } from "react";
import ItemList from "./components/ItemList";
import "./components/styles/App.css";
import { ItemType } from "./types";

export default function App() {
  const [itemList, setItemList] = useState<ItemType[]>([]);

  function addItem(item: ItemType) {
    setItemList([...itemList, item]);
  }

  function modifyItemList(newList: ItemType[]) {
    setItemList([...newList]);
  }

  return (
    <div className="app-container">
      <ItemList
        onModifyItemList={modifyItemList}
        itemList={itemList}
        onAddItem={addItem}
      />
    </div>
  );
}
