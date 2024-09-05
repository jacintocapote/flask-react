import User from "@/components/Dashboard/User";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLaout";
import React from "react";
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";

export const metadata: Metadata = {
  title: "Users manage | Bank - Admin",
  description: "Page for manage users",
  // other metadata
};

const UserPage: React.FC = () => {
  return (
    <DefaultLayout>
      <Breadcrumb pageName="Users" />
      <User/>
      
 
    </DefaultLayout>
  );
};

export default UserPage;
