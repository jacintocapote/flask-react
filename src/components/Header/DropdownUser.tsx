import { useState } from "react";
import Image from "next/image";
import ClickOutside from "@/components/ClickOutside";

const DropdownUser = () => {
  const [dropdownOpen, setDropdownOpen] = useState(false);

  return (
    <ClickOutside onClick={() => setDropdownOpen(false)} className="relative">
        <span className="h-12 w-12 rounded-full">
          <Image
            width={112}
            height={112}
            src="/images/user/user-03.png"
            style={{
              width: "auto",
              height: "auto",
            }}
            alt="User"
            className="overflow-hidden rounded-full"
          />
        </span>

        <span className="flex items-center gap-2 font-medium text-dark dark:text-dark-6">
          <span className="hidden lg:block">Administrator</span>
        </span>
    </ClickOutside>
  );
};

export default DropdownUser;
