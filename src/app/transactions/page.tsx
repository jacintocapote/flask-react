import Transaction from "@/components/Dashboard/Transaction";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLaout";
import React from "react";
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";

export const metadata: Metadata = {
  title: "Accounts manage | Bank - Admin",
  description: "Page for manage accounts",
  // other metadata
};

const UserPage: React.FC = () => {
  return (
    <DefaultLayout>
      <Breadcrumb pageName="Transactions" />
      <Transaction/>
      
 
    </DefaultLayout>
  );
};

export default UserPage;
