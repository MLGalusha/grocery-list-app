import { useState } from "react";
import ItemList from "./components/ItemList";
import "./components/styles/App.css";
import { Item } from "./types";

export default function App() {
  const [itemList, setItemList] = useState<Item[]>([]);

  function addItem(item: Item) {
    setItemList([...itemList, item]);
  }

  function modifyItemList(newList: Item[]) {
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
